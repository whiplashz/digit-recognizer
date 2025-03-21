import numpy as np

from utils.constants import EPS


def exclude_zero(X):
    X[X == 0] = EPS
    return X


def add_bias_ones(X):
    return np.vstack([X, np.ones(X.shape[1])])


def make_one_hot(x):
    unique = np.unique(x)
    n, m = len(unique), len(x)

    def to_one_hot(x_i):
        oh = np.zeros(n)
        oh[np.argmax(unique == x_i)] = 1
        return oh

    return np.apply_along_axis(to_one_hot, 0, x.reshape(1, -1))
