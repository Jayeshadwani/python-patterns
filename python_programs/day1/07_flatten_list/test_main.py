from main import flatten


def test_basic():
    assert flatten([1, [2, [3]]]) == [1, 2, 3]


def test_deeper():
    assert flatten([[1, 2], [3, [4, [5, [6]]]]]) == [1, 2, 3, 4, 5, 6]


def test_already_flat():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_empty():
    assert flatten([]) == []


def test_only_empty_lists():
    assert flatten([[], [[]]]) == []


def test_strings_are_single_items():
    assert flatten(["ab", ["cd"]]) == ["ab", "cd"]


def test_tuples_and_none_kept():
    assert flatten([(1, 2), [None, [{"k": 1}]]]) == [(1, 2), None, {"k": 1}]


def test_order_preserved():
    assert flatten([3, [1, [2]], 0]) == [3, 1, 2, 0]


def test_input_not_mutated():
    nested = [1, [2, [3]]]
    flatten(nested)
    assert nested == [1, [2, [3]]]


def test_depth_100():
    nested = 0
    for _ in range(100):
        nested = [nested]
    assert flatten(nested) == [0]