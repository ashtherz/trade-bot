from alpaca_trade_api import REST
from loguru import logger
from typing import Optional
from config.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY

api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url='https://paper-api.alpaca.markets')

def execute_trade(signal: str, 
                 symbol: str, 
                 risk_pct: float = 0.02,
                 stop_loss: Optional[float] = None) -> bool:
    """
    Execute a trade with position sizing and optional stop loss.
    
    Args:
        signal: 'BUY' or 'SELL'
        symbol: Stock symbol
        risk_pct: Maximum risk per trade as percentage of equity
        stop_loss: Optional stop loss price
    
    Returns:
        Boolean indicating if trade was executed successfully
    """
    try:
        account = api.get_account()
        equity = float(account.equity)
        max_risk = equity * risk_pct
        
        latest_trade = api.get_latest_trade(symbol)
        price = float(latest_trade.price)
        qty = int(max_risk / price)  # Ensure integer shares
        
        if qty > 0:
            order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side=signal.lower(),
                type='market',
                time_in_force='gtc'
            )
            
            if stop_loss and signal == 'BUY':
                api.submit_order(
                    symbol=symbol,
                    qty=qty,
                    side='sell',
                    type='stop',
                    time_in_force='gtc',
                    stop_price=stop_loss
                )
            
            logger.info(f"Executed {signal} order for {qty} shares of {symbol}")
            return True
            
    except Exception as e:
        logger.error(f"Trade execution failed: {str(e)}")
        return False 