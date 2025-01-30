from config.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY
from alpaca_trade_api import REST
import sys
import requests
import json

def test_connection():
    try:
        # Create headers for direct API request
        headers = {
            'APCA-API-KEY-ID': ALPACA_API_KEY,
            'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY,
            'User-Agent': 'Mozilla/5.0',  # Add user agent
            'Accept': 'application/json'   # Explicitly request JSON
        }
        
        # Try direct request first
        base_url = 'https://paper-api.alpaca.markets/v2'
        response = requests.get(
            f'{base_url}/account',
            headers=headers,
            verify=True  # Enable SSL verification
        )
        
        print("\nAPI Response Details:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Raw Response: {response.text[:1000]}")  # Print first 1000 chars
        
        if response.status_code == 200:
            account_data = response.json()
            print("\nConnection successful!")
            print(f"Account ID: {account_data.get('id')}")
            print(f"Status: {account_data.get('status')}")
            print(f"Buying Power: ${account_data.get('buying_power')}")
        else:
            print(f"\nError: Received status code {response.status_code}")
            print("Response:", response.text)
            
    except requests.exceptions.SSLError as e:
        print("\nSSL Error occurred. Try these fixes:")
        print("1. Update your certificates:")
        print("   cd /Applications/Python\\ 3.11/")
        print("   ./Install\\ Certificates.command")
        print("2. Or use a different endpoint")
        print(f"\nError details: {e}")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting steps:")
        print("1. Check if you're behind a VPN or proxy")
        print("2. Verify your internet connection")
        print("3. Ensure API keys are correct")
        print("4. Try using a different network")
        
        import traceback
        print("\nFull error traceback:")
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    print("Testing Alpaca API connection...")
    print(f"API Key: {ALPACA_API_KEY[:4]}...{ALPACA_API_KEY[-4:] if ALPACA_API_KEY else 'None'}")
    print(f"Secret Key: {ALPACA_SECRET_KEY[:4]}...{ALPACA_SECRET_KEY[-4:] if ALPACA_SECRET_KEY else 'None'}")
    test_connection() 