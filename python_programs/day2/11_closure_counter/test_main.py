from main import make_counter


def test_first_call():
    assert make_counter()() == 1


def test_sequence():
    c = make_counter()
    assert [c(), c(), c()] == [1, 2, 3]


def test_start():
    c = make_counter(start=10)
    assert [c(), c()] == [11, 12]


def test_step():
    c = make_counter(step=5)
    assert [c(), c()] == [5, 10]


def test_start_and_step():
    c = make_counter(start=10, step=5)
    assert [c(), c()] == [15, 20]


def test_negative_step():
    c = make_counter(step=-1)
    assert [c(), c()] == [-1, -2]


def test_zero_step():
    c = make_counter(start=7, step=0)
    assert [c(), c()] == [7, 7]


def test_counters_are_independent():
    a, b = make_counter(), make_counter()
    a()
    a()
    assert b() == 1
    assert a() == 3


def test_new_counter_starts_fresh():
    c = make_counter()
    c()
    c()
    assert make_counter()() == 1


def test_is_a_closure():
    c = make_counter()
    assert c.__closure__ is not None