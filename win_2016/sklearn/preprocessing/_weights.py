import numpy as np
from ..utils.fixes import bincount


def _balance_weights(y):
    """Compute sample weights such that the class distribution of y becomes
       balanced.

    Parameters
    ----------
    y : array-like
        Labels for the samples.

    Returns
    -------
    weights : array-like
        The sample weights.
    """
    y = np.asarray(y)
    y = np.searchsorted(np.unique(y), y)
    bins = bincount(y)

    weights = 1. / bins.take(y)
    weights *= bins.min()

    return weights
