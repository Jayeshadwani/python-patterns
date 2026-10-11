import numpy as np


def one_hot(labels: np.ndarray, num_classes: int) -> np.ndarray:
    """Return the (n, num_classes) one-hot matrix for labels."""
    one_hot_enc = np.zeros((len(labels),num_classes))

    one_hot_enc[np.arange(len(labels)),labels] = 1    
    
    return one_hot_enc


def main():
    print(one_hot(np.array([0, 2, 1]), 3))


if __name__ == "__main__":
    main()
