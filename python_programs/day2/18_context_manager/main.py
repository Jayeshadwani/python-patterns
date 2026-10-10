
import time
from contextlib import contextmanager


class Timer:
    def __init__(self):
        self.elapsed = None
        self._start = None

    def __enter__(self):
        self.elapsed = None
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self._start
        return False


@contextmanager
def swallow(*exc_types):
    try:
        yield
    except exc_types:
        pass


def main():
    with Timer() as t:
        time.sleep(0.05)

    print(f"Elapsed: {t.elapsed:.4f} seconds")

    with swallow(KeyError):
        {}["missing"]
        print("This line will not run")

    print("Still running")

    with swallow(KeyError):
        int("x")  # ValueError is not suppressed


if __name__ == "__main__":
    main()