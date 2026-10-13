import numpy as np
from main import rolling_mean


def test_known():
    assert np.allclose(rolling_mean(np.array([1.0, 2, 3, 4, 5]), 2), [1.5, 2.5, 3.5, 4.5])


def test_length():
    assert len(rolling_mean(np.arange(10.0), 4)) == 7


def test_window_one_is_identity():
    x = np.random.default_rng(7).normal(size=20)
    assert np.allclose(rolling_mean(x, 1), x)


def test_window_full_length():
    x = np.array([1.0, 2.0, 6.0])
    assert np.allclose(rolling_mean(x, 3), [3.0])


def test_matches_convolve():
    x = np.random.default_rng(7).normal(size=50)
    for w in (2, 3, 10, 50):
        assert np.allclose(rolling_mean(x, w), np.convolve(x, np.ones(w) / w, mode="valid"))
