from main import merge_dicts


def test_basic():
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}


def test_first_empty():
    assert merge_dicts({}, {"x": 1}) == {"x": 1}


def test_second_empty():
    assert merge_dicts({"x": 1}, {}) == {"x": 1}


def test_both_empty():
    assert merge_dicts({}, {}) == {}


def test_no_overlap():
    assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_all_overlap():
    assert merge_dicts({"a": 1, "b": 2}, {"a": 10, "b": 20}) == {"a": 11, "b": 22}


def test_zero_sum_key_kept():
    assert merge_dicts({"a": 2}, {"a": -2}) == {"a": 0}


def test_floats():
    assert merge_dicts({"a": 0.5}, {"a": 0.25}) == {"a": 0.75}


def test_inputs_not_mutated():
    a, b = {"a": 1}, {"a": 2, "b": 3}
    merge_dicts(a, b)
    assert a == {"a": 1}
    assert b == {"a": 2, "b": 3}


def test_returns_new_dict():
    a = {"a": 1}
    assert merge_dicts(a, {}) is not a