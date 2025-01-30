import numpy as np
from typing import Union, Optional
import pandas as pd

def monte_carlo_sim(S0: float, 
                   mu: float, 
                   sigma: float, 
                   days: int = 252, 
                   sims: int = 1000) -> np.ndarray:
    """
    Run Monte Carlo simulation for price paths.
    
    Args:
        S0: Initial stock price
        mu: Expected return (annualized)
        sigma: Volatility (annualized)
        days: Number of trading days to simulate
        sims: Number of simulation paths
    
    Returns:
        Array of simulated price paths
    """
    dt = 1/days
    paths = np.zeros((days, sims))
    paths[0] = S0
    
    for t in range(1, days):
        shock = np.random.normal(mu*dt, sigma*np.sqrt(dt), sims)
        paths[t] = paths[t-1] * np.exp(shock)
    
    return paths

def calculate_var(paths: np.ndarray, 
                 confidence_level: float = 0.95) -> float:
    """
    Calculate Value at Risk from simulation paths.
    
    Args:
        paths: Array of simulated price paths
        confidence_level: VaR confidence level
    
    Returns:
        VaR value
    """
    returns = (paths[-1] - paths[0]) / paths[0]
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return -var * paths[0] 