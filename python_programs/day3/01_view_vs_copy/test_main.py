import numpy as np
from main import reshape_view, reshape_copy, reshape_shares_memory


def test_view_shape():
    assert reshape_view(np.arange(6)).shape == (2, 3)


def test_view_shares_memory():
    a = np.arange(6)
    v = reshape_view(a)
    v[0, 0] = 99
    assert a[0] == 99


def test_copy_shape():
    assert reshape_copy(np.arange(6)).shape == (2, 3)


def test_copy_is_independent():
    a = np.arange(6)
    c = reshape_copy(a)
    c[0, 0] = -1
    assert a[0] == 0


def test_answer_is_true():
    assert reshape_shares_memory() is True
