import time

import pytest

from main import timer


def test_returns_result_and_passes_args():
    @timer
    def add(a, b=0):
        return a + b

    assert add(1, b=2) == 3
    assert add(4, 5) == 9


def test_last_elapsed_none_before_first_call():
    @timer
    def f():
        return 1

    # is checks whether two variables point to the same object in memory, while == checks whether the values of two variables are equal.
    # in checks whether an element exists in a collection (like a list, tuple, string, set, or dictionary).
    assert f.last_elapsed == 0.0


def test_records_duration():
    @timer
    def slow():
        time.sleep(0.05)

    slow()
    assert 0.045 <= slow.last_elapsed < 0.5


def test_last_elapsed_updates_each_call():
    @timer
    def sleeper(t):
        time.sleep(t)

    sleeper(0.05)
    first = sleeper.last_elapsed
    sleeper(0.0)
    assert sleeper.last_elapsed < first


def test_keeps_name_and_doc():
    @timer
    def documented():
        """My docstring."""

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "My docstring."


def test_exception_propagates_and_time_recorded():
    @timer
    def boom():
        time.sleep(0.02)
        raise ValueError("bad")

    with pytest.raises(ValueError):
        boom()
    assert boom.last_elapsed >= 0.015


def test_no_args_function():
    @timer
    def hello():
        return "hi"

    assert hello() == "hi"


def test_kwargs_only():
    @timer
    def greet(*, name):
        return f"hi {name}"

    assert greet(name="sam") == "hi sam"


def test_two_decorated_functions_independent():
    @timer
    def a():
        time.sleep(0.03)

    @timer
    def b():
        pass

    a()
    b()
    assert a.last_elapsed > b.last_elapsed