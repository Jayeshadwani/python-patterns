import numpy as np
from main import center_columns


def test_shape():
    assert center_columns(np.ones((5, 3))).shape == (5, 3)


def test_column_means_are_zero():
    X = np.random.default_rng(0).normal(5, 2, size=(50, 4))
    assert np.allclose(center_columns(X).mean(axis=0), 0)


def test_known_values():
    X = np.array([[1.0, 10.0], [3.0, 20.0]])
    assert np.allclose(center_columns(X), [[-1, -5], [1, 5]])


def test_input_not_modified():
    X = np.arange(12, dtype=float).reshape(4, 3)
    before = X.copy()
    center_columns(X)
    assert np.array_equal(X, before)
