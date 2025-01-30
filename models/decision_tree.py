from typing import Optional, Tuple
import numpy as np

def probability_tree(current_price: float, 
                    predicted_price: float, 
                    regime: int,
                    volatility: Optional[float] = None) -> Tuple[str, float]:
    """
    Generate trading signal using probability tree analysis.
    
    Args:
        current_price: Current asset price
        predicted_price: Model's price prediction
        regime: Market regime (0: bullish, 1: bearish)
        volatility: Optional historical volatility
    
    Returns:
        Tuple of (trading_signal, confidence_score)
    """
    # Calculate price change percentage
    price_change = (predicted_price - current_price) / current_price
    
    # Base confidence on regime and price change
    if regime == 0:  # Bullish regime
        if price_change > 0.02:  # 2% potential upside
            confidence = min(0.9, abs(price_change) * 10)
            return 'BUY', confidence
        elif price_change < -0.02:  # Unexpected bearish move in bull regime
            confidence = min(0.7, abs(price_change) * 5)
            return 'SELL', confidence
    else:  # Bearish regime
        if price_change < -0.02:  # 2% potential downside
            confidence = min(0.9, abs(price_change) * 10)
            return 'SELL', confidence
        elif price_change > 0.02:  # Unexpected bullish move in bear regime
            confidence = min(0.7, abs(price_change) * 5)
            return 'BUY', confidence
    
    return 'HOLD', 0.0 