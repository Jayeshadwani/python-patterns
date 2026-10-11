import numpy as np
from main import one_hot


def test_known():
    out = one_hot(np.array([0, 2, 1]), 3)
    assert np.array_equal(out, [[1, 0, 0], [0, 0, 1], [0, 1, 0]])


def test_shape_and_dtype():
    out = one_hot(np.array([1, 0]), 4)
    assert out.shape == (2, 4)
    assert out.dtype.kind == "f"


def test_each_row_sums_to_one():
    labels = np.random.default_rng(4).integers(0, 10, size=100)
    assert np.all(one_hot(labels, 10).sum(axis=1) == 1)


def test_argmax_recovers_labels():
    labels = np.random.default_rng(4).integers(0, 10, size=100)
    assert np.array_equal(one_hot(labels, 10).argmax(axis=1), labels)


def test_unused_classes_are_zero_columns():
    out = one_hot(np.array([0, 0]), 4)
    assert out[:, 1:].sum() == 0
