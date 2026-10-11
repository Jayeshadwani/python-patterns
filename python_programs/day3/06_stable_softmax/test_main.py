import numpy as np
from main import softmax, logsumexp


def test_softmax_matches_naive_on_small_input():
    x = np.random.default_rng(5).normal(size=(4, 5))
    naive = np.exp(x) / np.exp(x).sum(axis=1, keepdims=True)
    assert np.allclose(softmax(x, axis=1), naive)


def test_softmax_sums_to_one():
    x = np.random.default_rng(6).normal(size=(3, 4))
    assert np.allclose(softmax(x, axis=0).sum(axis=0), 1)
    assert np.allclose(softmax(x, axis=1).sum(axis=1), 1)


def test_softmax_large_values_are_finite():
    s = softmax(np.array([1000.0, 1001.0, 1002.0]))
    assert np.all(np.isfinite(s))
    assert np.isclose(s.sum(), 1.0)


def test_logsumexp_matches_naive_on_small_input():
    x = np.random.default_rng(5).normal(size=(4, 5))
    assert np.allclose(logsumexp(x, axis=1), np.log(np.exp(x).sum(axis=1)))


def test_logsumexp_large_values():
    x = np.array([1000.0, 1001.0, 1002.0])
    expected = 1002 + np.log(1 + np.exp(-1) + np.exp(-2))
    assert np.isclose(logsumexp(x), expected)


def test_logsumexp_removes_axis():
    x = np.random.default_rng(6).normal(size=(3, 4))
    assert logsumexp(x, axis=0).shape == (4,)
    assert logsumexp(x, axis=1).shape == (3,)
