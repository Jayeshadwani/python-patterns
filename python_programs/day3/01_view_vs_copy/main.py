import numpy as np


def reshape_view(a: np.ndarray) -> np.ndarray:
    """Return a as shape (2, 3), sharing memory with a."""
    return a.reshape(2, 3)


def reshape_copy(a: np.ndarray) -> np.ndarray:
    """Return a as shape (2, 3), independent of a."""
    return a.copy().reshape(2, 3)


def reshape_shares_memory(a: np.ndarray) -> bool:
    """Does a.reshape(2, 3) share memory with a contiguous a?"""
    return np.shares_memory(reshape_view(a), a)


def main():
    a = np.arange(6)
    v = reshape_view(a)
    v[0, 0] = 99
    print("a after writing to the view:", a)
    print("shares memory:", reshape_shares_memory(a))


if __name__ == "__main__":
    main()
