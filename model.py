import numpy as np

def process(attr: np.ndarray, pred: np.ndarray, weights:np.ndarray = None):
    if isinstance(weights, np.ndarray):
        assert weights
