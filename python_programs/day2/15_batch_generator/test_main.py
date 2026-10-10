import inspect
from itertools import count, islice

import pytest

from main import batch


def test_is_a_generator():
    assert inspect.isgenerator(batch([1, 2, 3], 2))


def test_basic_with_short_last_batch():
    assert list(batch([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_exact_multiple_has_no_trailing_empty_batch():
    assert list(batch([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_empty_input():
    assert list(batch([], 3)) == []


def test_n_larger_than_input():
    assert list(batch([1, 2], 10)) == [[1, 2]]


def test_n_equals_one():
    assert list(batch([1, 2, 3], 1)) == [[1], [2], [3]]


def test_strings_are_iterables():
    assert list(batch("abcde", 2)) == [["a", "b"], ["c", "d"], ["e"]]


def test_batches_are_lists_and_independent():
    batches = list(batch(range(6), 2))
    assert batches == [[0, 1], [2, 3], [4, 5]]
    assert all(type(b) is list for b in batches)


def test_works_on_infinite_input():
    assert list(islice(batch(count(), 3), 2)) == [[0, 1, 2], [3, 4, 5]]


def test_reads_source_only_as_needed():
    consumed = []

    def source():
        for i in range(100):
            consumed.append(i)
            yield i

    g = batch(source(), 3)
    assert next(g) == [0, 1, 2]
    assert len(consumed) == 3


def test_invalid_n():
    with pytest.raises(ValueError):
        list(batch([1, 2, 3], 0))
    with pytest.raises(ValueError):
        list(batch([1, 2, 3], -2))