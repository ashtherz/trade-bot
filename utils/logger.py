from loguru import logger
import os
from datetime import datetime

# Configure logger
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Remove default logger and add custom configuration
logger.remove()
logger.add(
    os.path.join(log_dir, "trade_{time}.log"),
    rotation="1 day",
    retention="1 month",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO"
)

def log_trade(symbol: str, 
              action: str, 
              quantity: int, 
              price: float, 
              confidence: float):
    """
    Log trade details.
    
    Args:
        symbol: Trading symbol
        action: 'BUY' or 'SELL'
        quantity: Number of shares
        price: Execution price
        confidence: Model confidence score
    """
    logger.info(
        f"TRADE | {symbol} | {action} | Qty: {quantity} | "
        f"Price: ${price:.2f} | Confidence: {confidence:.2f}"
    )

def log_error(error_msg: str, context: str = ""):
    """Log error messages with context"""
    logger.error(f"{context} | {error_msg}")

def log_model_metrics(model_name: str, metrics: dict):
    """Log model performance metrics"""
    logger.info(f"MODEL METRICS | {model_name} | {metrics}") 