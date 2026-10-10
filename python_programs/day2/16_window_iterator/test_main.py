import pytest

from main import SlidingWindow, WindowIterator


def test_basic_windows():
    assert list(SlidingWindow([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]


def test_windows_are_tuples():
    assert all(type(w) is tuple for w in SlidingWindow([1, 2, 3], 2))


def test_strings():
    assert list(SlidingWindow("abcd", 3)) == [("a", "b", "c"), ("b", "c", "d")]


def test_size_equals_length():
    assert list(SlidingWindow([1, 2, 3], 3)) == [(1, 2, 3)]


def test_size_larger_than_data():
    assert list(SlidingWindow([1, 2], 5)) == []


def test_empty_data():
    assert list(SlidingWindow([], 2)) == []


def test_size_one():
    assert list(SlidingWindow([7, 8], 1)) == [(7,), (8,)]


def test_invalid_size():
    with pytest.raises(ValueError):
        SlidingWindow([1, 2, 3], 0)
    with pytest.raises(ValueError):
        SlidingWindow([1, 2, 3], -1)


def test_can_loop_twice():
    w = SlidingWindow([1, 2, 3], 2)
    assert list(w) == [(1, 2), (2, 3)]
    assert list(w) == [(1, 2), (2, 3)]


def test_iter_returns_a_new_iterator_each_time():
    w = SlidingWindow([1, 2, 3], 2)
    assert iter(w) is not iter(w)
    assert isinstance(iter(w), WindowIterator)


def test_two_iterators_are_independent():
    w = SlidingWindow([1, 2, 3, 4], 2)
    a, b = iter(w), iter(w)
    assert next(a) == (1, 2)
    assert next(a) == (2, 3)
    assert next(b) == (1, 2)


def test_iterator_returns_itself_from_iter():
    it = iter(SlidingWindow([1, 2, 3], 2))
    assert iter(it) is it


def test_manual_protocol_and_stop_iteration():
    it = iter(SlidingWindow([1, 2, 3], 2))
    assert next(it) == (1, 2)
    assert next(it) == (2, 3)
    with pytest.raises(StopIteration):
        next(it)
    with pytest.raises(StopIteration):
        next(it)