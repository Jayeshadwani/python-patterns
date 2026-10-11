import numpy as np


def pairwise_distances(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Return the (n, m) matrix of Euclidean distances between rows of A and B."""
    # A = (n,d) shape
    # B = (m,d) shape
    # C = (n, m) shape, eliminate the d axis by summing over it,
    # broadcasting in play, n/1 == m/1 and d == d
    A_reshaped = A.reshape((A.shape[0],1,A.shape[1])) # (n,1,d)
    B_reshaped = B.reshape((1,B.shape[0],B.shape[1])) # (1,m,d)
    # Euclidean distance formula: sqrt(sum((A-B)^2))
    C = np.sqrt(np.sum((A_reshaped - B_reshaped) ** 2, axis=2)) # (n,m)
    return C



def main():
    A = np.array([[0.0, 0.0], [3.0, 4.0]])
    B = np.array([[0.0, 0.0]])
    #print(A.shape,B.shape)
    print(pairwise_distances(A, B))


if __name__ == "__main__":
    main()
