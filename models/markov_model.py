from hmmlearn import hmm
import numpy as np
import pandas as pd
from typing import Tuple

def train_markov_model(data: pd.DataFrame, n_states: int = 2) -> Tuple[hmm.GaussianHMM, pd.DataFrame]:
    """
    Train a Hidden Markov Model for market regime detection.
    
    Args:
        data: DataFrame with market data
        n_states: Number of market regimes to detect
    
    Returns:
        Tuple of (trained model, DataFrame with regime predictions)
    """
    returns = data['Returns'].values.reshape(-1, 1)
    model = hmm.GaussianHMM(n_components=n_states, covariance_type="diag")
    model.fit(returns)
    data['Regime'] = model.predict(returns)
    return model, data 