from typing import Callable


def make_counter(start: int = 0, step: int = 1) -> Callable[[], int]:
    """Return a function that adds step to a private count and returns the new count."""
    count = start
    def counter() -> int:
        # Use the nonlocal keyword to modify the count variable from the enclosing scope
        nonlocal count # tells Python where the count variable is defined, so we can modify it
        count += step
        return count
    return counter


def main():
    c = make_counter()
    print(c(), c(), c())
    d = make_counter(start=10, step=5)
    print(d(), d())


if __name__ == "__main__":
    main()