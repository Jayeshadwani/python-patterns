from main import add_item


def test_first_call():
    assert add_item(1) == [1]


def test_calls_are_independent():
    add_item("a")
    assert add_item("b") == ["b"]


def test_many_default_calls_stay_length_one():
    for i in range(5):
        assert add_item(i) == [i]


def test_appends_to_passed_list():
    lst = []
    add_item(1, lst)
    add_item(2, lst)
    assert lst == [1, 2]


def test_returns_same_object():
    lst = [10]
    assert add_item(20, lst) is lst
    assert lst == [10, 20]


def test_explicit_empty_list_is_used():
    lst = []
    result = add_item(1, lst)
    assert result is lst
    assert lst == [1]


def test_default_calls_return_different_lists():
    assert add_item(1) is not add_item(1)


def test_passed_list_unaffected_by_default_calls():
    lst = [5]
    add_item(1)
    add_item(2)
    assert lst == [5]
