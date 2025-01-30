import yfinance as yf
import pandas as pd
from typing import Optional

def fetch_data(ticker: str, start: str, end: Optional[str] = None) -> pd.DataFrame:
    """
    Fetch historical market data from Yahoo Finance.
    
    Args:
        ticker: Stock symbol
        start: Start date in 'YYYY-MM-DD' format
        end: End date in 'YYYY-MM-DD' format (optional)
    
    Returns:
        DataFrame with OHLCV data and calculated returns
    """
    data = yf.download(ticker, start=start, end=end)
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    data['Returns'] = data['Close'].pct_change()
    return data.dropna() 