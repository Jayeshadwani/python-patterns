from main import two_sum


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_not_same_element_twice():
    assert two_sum([3, 2, 4], 6) == (1, 2)


def test_duplicates():
    assert two_sum([3, 3], 6) == (0, 1)


def test_no_pair():
    assert two_sum([1, 2, 3], 10) is None


def test_negatives():
    assert two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)


def test_zeros():
    assert two_sum([0, 4, 3, 0], 0) == (0, 3)


def test_empty_and_single():
    assert two_sum([], 5) is None
    assert two_sum([5], 5) is None