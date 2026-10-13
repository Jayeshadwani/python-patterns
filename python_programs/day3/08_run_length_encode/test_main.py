import numpy as np
from main import run_length_encode


def test_example():
    v, n = run_length_encode(np.array([1, 1, 2, 2, 2, 3]))
    assert list(v) == [1, 2, 3]
    assert list(n) == [2, 3, 1]


def test_single_run():
    v, n = run_length_encode(np.array([7, 7, 7]))
    assert list(v) == [7]
    assert list(n) == [3]


def test_single_element():
    v, n = run_length_encode(np.array([5]))
    assert list(v) == [5]
    assert list(n) == [1]


def test_alternating():
    v, n = run_length_encode(np.array([1, 0, 1, 0]))
    assert list(v) == [1, 0, 1, 0]
    assert list(n) == [1, 1, 1, 1]


def test_empty():
    v, n = run_length_encode(np.array([], dtype=int))
    assert len(v) == 0
    assert len(n) == 0


def test_roundtrip():
    x = np.random.default_rng(8).integers(0, 3, size=200)
    v, n = run_length_encode(x)
    assert np.array_equal(np.repeat(v, n), x)
