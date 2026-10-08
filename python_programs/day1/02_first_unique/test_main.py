from main import first_unique


def test_middle_char():
    assert first_unique("aabc") == "b"


def test_no_unique():
    assert first_unique("aabb") is None


def test_empty():
    assert first_unique("") is None


def test_unique_in_middle():
    assert first_unique("xyx") == "y"


def test_first_char_unique():
    assert first_unique("abc") == "a"


def test_last_char_unique():
    assert first_unique("aabbc") == "c"


def test_space_is_a_char():
    assert first_unique("aa bb") == " "