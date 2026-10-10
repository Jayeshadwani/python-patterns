import pytest

from main import retry


def make_flaky(fail_times, exc=ConnectionError):
    state = {"calls": 0}

    def f(*args, **kwargs):
        state["calls"] += 1
        if state["calls"] <= fail_times:
            raise exc(f"fail {state['calls']}")
        return ("ok", args, kwargs)

    return f, state


def test_success_first_try():
    f, state = make_flaky(0)
    assert retry(3)(f)(1, x=2) == ("ok", (1,), {"x": 2})
    assert state["calls"] == 1


def test_fails_twice_then_succeeds():
    f, state = make_flaky(2)
    assert retry(3)(f)()[0] == "ok"
    assert state["calls"] == 3


def test_always_fails_raises_last_exception():
    f, state = make_flaky(99)
    with pytest.raises(ConnectionError, match="fail 3"):
        retry(3)(f)()
    assert state["calls"] == 3


def test_unlisted_exception_not_retried():
    f, state = make_flaky(99, exc=ValueError)
    with pytest.raises(ValueError):
        retry(5, exceptions=(KeyError,))(f)()
    assert state["calls"] == 1


def test_tuple_of_exceptions():
    f, state = make_flaky(2, exc=KeyError)
    assert retry(3, exceptions=(KeyError, ValueError))(f)()[0] == "ok"
    assert state["calls"] == 3


def test_max_attempts_one_means_no_retry():
    f, state = make_flaky(1)
    with pytest.raises(ConnectionError):
        retry(1)(f)()
    assert state["calls"] == 1


def test_keeps_name_and_doc():
    @retry(2)
    def documented():
        """My docstring."""

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "My docstring."


def test_invalid_max_attempts():
    with pytest.raises(ValueError):
        retry(0)
    with pytest.raises(ValueError):
        retry(-1)


def test_each_invocation_starts_fresh():
    f, state = make_flaky(99)
    g = retry(3)(f)
    for _ in range(2):
        with pytest.raises(ConnectionError):
            g()
    assert state["calls"] == 6


def test_works_with_at_syntax():
    state = {"n": 0}

    @retry(2)
    def sometimes():
        state["n"] += 1
        if state["n"] == 1:
            raise RuntimeError("first")
        return "done"

    assert sometimes() == "done"
    assert state["n"] == 2