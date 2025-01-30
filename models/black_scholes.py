import numpy as np
from scipy.stats import norm
from typing import Tuple

def black_scholes(S: float, 
                 K: float, 
                 T: float, 
                 r: float, 
                 sigma: float, 
                 option_type: str = 'call') -> Tuple[float, float, float]:
    """
    Calculate Black-Scholes option price and Greeks.
    
    Args:
        S: Current stock price
        K: Strike price
        T: Time to expiration (in years)
        r: Risk-free rate
        sigma: Volatility
        option_type: 'call' or 'put'
    
    Returns:
        Tuple of (option_price, delta, gamma)
    """
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    if option_type.lower() == 'call':
        price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
        delta = norm.cdf(d1)
    else:  # put
        price = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
        delta = -norm.cdf(-d1)
    
    gamma = norm.pdf(d1)/(S*sigma*np.sqrt(T))
    
    return price, delta, gamma 