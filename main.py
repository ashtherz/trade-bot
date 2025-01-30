import pandas as pd
from datetime import datetime, timedelta
from loguru import logger
import schedule
import time

from config.settings import SYMBOLS, RISK_PERCENTAGE
from data.data_loader import fetch_data
from models.markov_model import train_markov_model
from models.dl_model import train_fastai_model
from utils.risk_management import execute_trade

def trading_logic(symbol: str) -> None:
    """Main trading logic for a single symbol"""
    try:
        # Fetch recent data
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        df = fetch_data(symbol, start_date.strftime('%Y-%m-%d'))
        
        # Train models
        markov_model, df = train_markov_model(df)
        learn = train_fastai_model(df)
        
        # Get predictions
        latest_data = df.iloc[-1:].copy()
        pred, _ = learn.get_preds(dl=learn.dls.test_dl(latest_data))
        predicted_price = pred.item()
        
        # Generate trading signal
        current_price = df['Close'].iloc[-1]
        regime = df['Regime'].iloc[-1]
        
        # Simple trading rules
        if regime == 0:  # Bullish regime
            if predicted_price > current_price * 1.02:  # 2% potential upside
                execute_trade('BUY', symbol, RISK_PERCENTAGE)
        else:  # Bearish regime
            if predicted_price < current_price * 0.98:  # 2% potential downside
                execute_trade('SELL', symbol, RISK_PERCENTAGE)
                
    except Exception as e:
        logger.error(f"Error in trading logic for {symbol}: {str(e)}")

def main():
    """Main function to run the trading bot"""
    logger.info("Starting trading bot...")
    
    # Schedule trading runs
    for symbol in SYMBOLS:
        schedule.every().day.at("09:31").do(trading_logic, symbol)  # Just after market open
        
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main() 