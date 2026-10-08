from main import is_valid


def test_simple_pair():
    assert is_valid("()") is True


def test_three_types():
    assert is_valid("()[]{}") is True


def test_nested():
    assert is_valid("{[]}") is True


def test_wrong_type():
    assert is_valid("(]") is False


def test_wrong_order():
    assert is_valid("([)]") is False


def test_never_closed():
    assert is_valid("(") is False


def test_closes_nothing():
    assert is_valid(")") is False


def test_empty():
    assert is_valid("") is True


def test_closer_first():
    assert is_valid("}{") is False


def test_extra_opener_at_end():
    assert is_valid("(()") is False


def test_extra_closer_at_end():
    assert is_valid("())") is False


def test_deep_valid():
    assert is_valid("(" * 10000 + ")" * 10000) is True


def test_deep_one_missing():
    assert is_valid("(" * 10000 + ")" * 9999) is False