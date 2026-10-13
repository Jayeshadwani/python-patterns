import numpy as np


def run_length_encode(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (values, lengths) of the consecutive runs in x."""
    raise NotImplementedError


def main():
    print(run_length_encode(np.array([1, 1, 2, 2, 2, 3])))


if __name__ == "__main__":
    main()
