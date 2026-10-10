import inspect
import time
from itertools import islice

from main import fib_below, fibonacci


def reference_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def test_fibonacci_is_a_generator():
    assert inspect.isgenerator(fibonacci())


def test_first_ten():
    assert list(islice(fibonacci(), 10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_next_step_by_step():
    g = fibonacci()
    assert [next(g), next(g), next(g), next(g)] == [0, 1, 1, 2]


def test_generators_are_independent():
    a, b = fibonacci(), fibonacci()
    next(a)
    next(a)
    next(a)
    assert next(b) == 0


def test_infinite_and_exact_for_big_values():
    start = time.perf_counter()
    values = list(islice(fibonacci(), 1001))
    assert values[1000] == reference_fib(1000)
    assert time.perf_counter() - start < 1.0


def test_fib_below_is_a_generator():
    assert inspect.isgenerator(fib_below(10))


def test_fib_below_ten():
    assert list(fib_below(10)) == [0, 1, 1, 2, 3, 5, 8]


def test_fib_below_edges():
    assert list(fib_below(0)) == []
    assert list(fib_below(-5)) == []
    assert list(fib_below(1)) == [0]
    assert list(fib_below(2)) == [0, 1, 1]


def test_fib_below_is_strict():
    assert 13 not in list(fib_below(13))
    assert 13 in list(fib_below(14))


def test_fib_below_count_for_a_million():
    assert len(list(fib_below(10**6))) == 31


def test_generator_is_used_up_after_one_pass():
    g = fib_below(10)
    assert list(g) == [0, 1, 1, 2, 3, 5, 8]
    assert list(g) == []