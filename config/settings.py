import os
from dotenv import load_dotenv

load_dotenv()

# Update these to match Alpaca's expected environment variable names
ALPACA_API_KEY = os.getenv("APCA_API_KEY_ID")  # Changed from ALPACA_API_KEY
ALPACA_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")  # Changed from ALPACA_SECRET_KEY

# Trading parameters
RISK_PERCENTAGE = 0.02  # 2% risk per trade
DEFAULT_TIMEFRAME = '1D'
SYMBOLS = ['SPY']  # Add more symbols as needed 