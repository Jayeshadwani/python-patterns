import time

from main import dedupe


def test_basic():
    assert dedupe([3, 1, 3, 2]) == [3, 1, 2]


def test_strings():
    assert dedupe(["b", "a", "b"]) == ["b", "a"]


def test_all_same():
    assert dedupe([1, 1, 1]) == [1]


def test_empty():
    assert dedupe([]) == []


def test_no_duplicates():
    assert dedupe([5, 4, 3]) == [5, 4, 3]


def test_none_and_zero():
    assert dedupe([None, None, 0]) == [None, 0]


def test_int_and_str_differ():
    assert dedupe([1, "1", 1]) == [1, "1"]


def test_input_not_mutated():
    items = [2, 2, 1]
    dedupe(items)
    assert items == [2, 2, 1]


def test_returns_new_list():
    items = [1, 2]
    assert dedupe(items) is not items


def test_linear_time():
    items = list(range(50000)) * 2
    start = time.perf_counter()
    result = dedupe(items)
    elapsed = time.perf_counter() - start
    assert result == list(range(50000))
    assert elapsed < 1.0, f"too slow ({elapsed:.1f}s): is it O(n^2)?"