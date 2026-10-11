import numpy as np
from main import pairwise_distances


def test_shape():
    assert pairwise_distances(np.zeros((5, 3)), np.zeros((7, 3))).shape == (5, 7)


def test_3_4_5():
    A = np.array([[0.0, 0.0], [3.0, 4.0]])
    B = np.array([[0.0, 0.0]])
    assert np.allclose(pairwise_distances(A, B), [[0.0], [5.0]])


def test_zero_diagonal_and_symmetric():
    A = np.random.default_rng(2).normal(size=(6, 4))
    D = pairwise_distances(A, A)
    assert np.allclose(np.diag(D), 0)
    assert np.allclose(D, D.T)


def test_matches_loop():
    rng = np.random.default_rng(1)
    A, B = rng.normal(size=(5, 3)), rng.normal(size=(7, 3))
    D = pairwise_distances(A, B)
    for i in range(5):
        for j in range(7):
            assert np.isclose(D[i, j], np.sqrt(((A[i] - B[j]) ** 2).sum()))
