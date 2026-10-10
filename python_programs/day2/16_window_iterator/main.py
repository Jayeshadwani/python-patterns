from typing import Any, Sequence, Tuple


class WindowIterator:
    """Iterator over consecutive windows (tuples) of a sequence."""

    def __init__(self, data: Sequence[Any], size: int) -> None:
        self.data = data
        self.size = size
        self.index = 0

    def __iter__(self) -> "WindowIterator":
        return self

    # The __next__ method returns the next window of the specified size from the data sequence. If there are no more windows to return, it raises a StopIteration exception.
    def __next__(self) -> Tuple[Any, ...]:
        if self.index + self.size > len(self.data):
            raise StopIteration
        window = tuple(self.data[self.index: self.index + self.size])
        self.index += 1
        return window


class SlidingWindow:
    """Iterable that gives a fresh WindowIterator every time it is looped over."""

    def __init__(self, data: Sequence[Any], size: int) -> None:
        self.data = data
        self.size = size
        if size <= 0:
            raise ValueError("Window size must be positive.")

    def __iter__(self) -> WindowIterator:
        return WindowIterator(self.data, self.size)


def main():
    print(list(SlidingWindow([1, 2, 3, 4, 5], 3)))
    w = SlidingWindow("abcd", 2)
    def __init__(self, data: Sequence[Any], size: int) -> None:
        self.data = data
        self.size = size

    def __iter__(self) -> WindowIterator:
        return WindowIterator(self.data, self.size)


def main():
    print(list(SlidingWindow([1, 2, 3, 4, 5], 3)))
    w = SlidingWindow("abcd", 2)
    print(list(w), list(w))


if __name__ == "__main__":
    main()