import numpy as np


def center_columns(X: np.ndarray) -> np.ndarray:
    """Subtract each column's mean from X."""
    return X - np.mean(X, axis=0)


def main():
    X = np.array([[1.0, 10.0], [3.0, 20.0]])
    print("Original array:")
    print(X)
    print("Centered array:")
    print(center_columns(X))


if __name__ == "__main__":
    main()
