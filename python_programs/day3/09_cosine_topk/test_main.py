import numpy as np
from main import cosine_topk


def reference(Q, D, k):
    Qn = Q / np.linalg.norm(Q, axis=1, keepdims=True)
    Dn = D / np.linalg.norm(D, axis=1, keepdims=True)
    S = Qn @ Dn.T
    idx = np.argsort(-S, axis=1)[:, :k]
    return idx, np.take_along_axis(S, idx, axis=1)


def test_small_example():
    Q = np.array([[1.0, 0.0]])
    D = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    idx, sc = cosine_topk(Q, D, 2)
    assert list(idx[0]) == [0, 2]
    assert np.allclose(sc[0], [1.0, np.sqrt(0.5)])


def test_shapes():
    rng = np.random.default_rng(9)
    idx, sc = cosine_topk(rng.normal(size=(6, 8)), rng.normal(size=(40, 8)), 5)
    assert idx.shape == (6, 5)
    assert sc.shape == (6, 5)


def test_matches_full_sort():
    rng = np.random.default_rng(9)
    Q, D = rng.normal(size=(6, 8)), rng.normal(size=(40, 8))
    for k in (1, 5, 40):
        idx, sc = cosine_topk(Q, D, k)
        ridx, rsc = reference(Q, D, k)
        assert np.array_equal(idx, ridx)
        assert np.allclose(sc, rsc)


def test_scores_sorted_descending():
    rng = np.random.default_rng(10)
    _, sc = cosine_topk(rng.normal(size=(3, 5)), rng.normal(size=(20, 5)), 6)
    assert np.all(np.diff(sc, axis=1) <= 1e-12)


def test_scale_invariant():
    rng = np.random.default_rng(10)
    Q, D = rng.normal(size=(3, 5)), rng.normal(size=(20, 5))
    i1, s1 = cosine_topk(Q, D, 4)
    i2, s2 = cosine_topk(Q * 10, D * 0.1, 4)
    assert np.array_equal(i1, i2)
    assert np.allclose(s1, s2)
