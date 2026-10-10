import inspect
import time

import pytest

import main
from main import Timer, swallow


# ---------- Timer ----------

def test_enter_returns_the_timer_itself():
    timer = Timer()
    with timer as t:
        assert t is timer


def test_elapsed_none_before_and_during():
    timer = Timer()
    assert timer.elapsed is None
    with timer:
        assert timer.elapsed is None


def test_elapsed_measures_block():
    with Timer() as t:
        time.sleep(0.05)
    assert isinstance(t.elapsed, float)
    assert 0.04 <= t.elapsed < 0.5


def test_elapsed_set_and_exception_propagates():
    timer = Timer()
    with pytest.raises(RuntimeError, match="boom"):
        with timer:
            time.sleep(0.02)
            raise RuntimeError("boom")
    assert timer.elapsed is not None and timer.elapsed >= 0.01


def test_timer_reusable_overwrites_elapsed():
    timer = Timer()
    with timer:
        time.sleep(0.05)
    first = timer.elapsed
    with timer:
        pass
    assert timer.elapsed < first


def test_timer_is_a_class_with_protocol_methods():
    assert inspect.isclass(Timer)
    assert hasattr(Timer, "__enter__") and hasattr(Timer, "__exit__")


# ---------- swallow ----------

def test_swallow_is_decorated_generator_function():
    assert inspect.isgeneratorfunction(inspect.unwrap(main.swallow))


def test_swallow_suppresses_listed_type_and_continues():
    reached = False
    with swallow(ValueError):
        raise ValueError("x")
    reached = True
    assert reached


def test_swallow_skips_rest_of_block():
    ran = []
    with swallow(KeyError):
        ran.append("before")
        {}["k"]
        ran.append("after")
    assert ran == ["before"]


def test_swallow_other_exception_propagates():
    with pytest.raises(KeyError):
        with swallow(ValueError):
            {}["k"]


def test_swallow_multiple_types():
    with swallow(KeyError, ValueError):
        raise ValueError
    with swallow(KeyError, ValueError):
        raise KeyError("k")


def test_swallow_subclass_is_suppressed():
    with swallow(LookupError):
        {}["k"]  # KeyError is a LookupError


def test_swallow_no_types_suppresses_nothing():
    with pytest.raises(ValueError):
        with swallow():
            raise ValueError


def test_swallow_no_error_runs_normally():
    out = []
    with swallow(ValueError):
        out.append(1)
    assert out == [1]