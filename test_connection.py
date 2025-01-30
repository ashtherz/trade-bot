from config.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY
from alpaca_trade_api import REST
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
import warnings
import os

# Debug: Print environment variables
print("Environment variables:")
print(f"APCA_API_KEY_ID: {os.getenv('APCA_API_KEY_ID')}")
print(f"APCA_API_SECRET_KEY: {os.getenv('APCA_API_SECRET_KEY')}")

# Suppress SSL verification warnings
warnings.filterwarnings('ignore', category=InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

def test_connection():
    try:
        # Create a session with SSL verification disabled
        session = requests.Session()
        session.verify = False
        
        # Add headers for debugging
        headers = {
            'APCA-API-KEY-ID': ALPACA_API_KEY,
            'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY
        }
        
        # Try a direct request first
        response = session.get(
            'https://paper-api.alpaca.markets/v2/account',
            headers=headers,
            verify=False
        )
        
        print("\nDirect API Response:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Content: {response.text}")
        
        # Now try with the REST client
        api = REST(
            key_id=ALPACA_API_KEY,
            secret_key=ALPACA_SECRET_KEY,
            base_url='https://paper-api.alpaca.markets',
            api_version='v2'
        )
        api._session = session
        
        print("\nTesting connection with:")
        print(f"API Key: {ALPACA_API_KEY[:4]}...{ALPACA_API_KEY[-4:] if ALPACA_API_KEY else 'None'}")
        print(f"Secret Key: {ALPACA_SECRET_KEY[:4]}...{ALPACA_SECRET_KEY[-4:] if ALPACA_SECRET_KEY else 'None'}")
        print(f"Base URL: {api._base_url}")
        
        account = api.get_account()
        print("\nConnection successful!")
        print(f"Account data: {account}")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting steps:")
        print("1. Verify API keys in .env file")
        print("2. Check if .env file is in the correct location")
        print("3. Ensure you're using paper trading keys")
        print("4. Try restarting your Python session")
        
        # Print the full error traceback for debugging
        import traceback
        print("\nFull error traceback:")
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    test_connection() 