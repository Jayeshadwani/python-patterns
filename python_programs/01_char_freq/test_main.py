from main import char_freq

def test_basic():
    assert char_freq("aab") == {"a": 2, "b": 1}

def test_empty():
    assert char_freq("") == {}

def test_space():
    assert char_freq("a b a") == {"a": 2, " ": 2, "b": 1}