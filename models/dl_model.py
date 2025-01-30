from fastai.tabular.all import *
from typing import List

def train_fastai_model(data: pd.DataFrame, 
                      dep_var: str = 'Close',
                      cont_names: List[str] = ['Open', 'High', 'Low', 'Volume', 'Returns']):
    """
    Train a deep learning model using Fast.ai.
    
    Args:
        data: DataFrame with market data
        dep_var: Target variable to predict
        cont_names: List of continuous features
    
    Returns:
        Trained Fast.ai learner
    """
    procs = [Categorify, FillMissing, Normalize]
    
    dls = TabularDataLoaders.from_df(
        data, 
        procs=procs, 
        cont_names=cont_names,
        y_names=dep_var, 
        bs=64, 
        valid_pct=0.2
    )
    
    learn = tabular_learner(dls, layers=[200, 100], metrics=rmse)
    learn.fit_one_cycle(5)
    return learn 