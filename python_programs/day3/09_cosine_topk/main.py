import numpy as np


def cosine_topk(Q: np.ndarray, D: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
    """Return (indices, scores) of the top-k cosine matches per query, best first."""
    raise NotImplementedError


def main():
    Q = np.array([[1.0, 0.0]])
    D = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    print(cosine_topk(Q, D, 2))


if __name__ == "__main__":
    main()
