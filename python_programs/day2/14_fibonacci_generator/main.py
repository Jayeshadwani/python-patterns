from itertools import islice
from typing import Iterator


def fibonacci() -> Iterator[int]:
    """Yield the Fibonacci numbers forever: 0,1, 1 2, 3, 5, ..."""

    a, b = 0, 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c


def fib_below(limit: int) -> Iterator[int]:
    """Yield the Fibonacci numbers strictly less than limit, then stop."""
    gen = fibonacci()
    while True:
        c = next(gen)
        if c >= limit:
            break
        yield c


def main():
    print("first 10:", list(islice(fibonacci(), 10)))
    print("below 100:", list(fib_below(100)))


if __name__ == "__main__":
    main()