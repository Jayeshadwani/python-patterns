import time

from main import top_k_frequent


def test_basic():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    assert top_k_frequent(words, 2) == ["i", "love"]


def test_four_words():
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    assert top_k_frequent(words, 4) == ["the", "is", "sunny", "day"]


def test_all_tied_alphabetical():
    assert top_k_frequent(["b", "a", "c"], 2) == ["a", "b"]


def test_tie_breaks_inside_top_k():
    assert top_k_frequent(["x", "y", "y", "x", "z"], 2) == ["x", "y"]


def test_k_larger_than_unique():
    assert top_k_frequent(["a", "b", "a"], 10) == ["a", "b"]


def test_k_equals_one():
    assert top_k_frequent(["a", "b", "b"], 1) == ["b"]


def test_k_zero():
    assert top_k_frequent(["a", "b"], 0) == []


def test_empty_words():
    assert top_k_frequent([], 3) == []


def test_single_word():
    assert top_k_frequent(["a"], 1) == ["a"]


def test_input_not_mutated():
    words = ["b", "a", "b"]
    top_k_frequent(words, 1)
    assert words == ["b", "a", "b"]


def test_large_input_is_fast():
    words = [f"w{i % 100000}" for i in range(300000)] + ["hot"] * 5
    start = time.perf_counter()
    result = top_k_frequent(words, 3)
    elapsed = time.perf_counter() - start
    assert result[0] == "hot"
    assert len(result) == 3
    assert elapsed < 2.0, f"too slow ({elapsed:.1f}s)"