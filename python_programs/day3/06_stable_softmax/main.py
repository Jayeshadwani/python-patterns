import numpy as np


def logsumexp(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Stable log(sum(exp(x))) along axis."""
    x_max = np.max(x, axis=axis, keepdims=True)
    result = x_max + np.log(np.sum(np.exp(x - x_max), axis=axis, keepdims=True))
    # Squeeze the result to remove the axis we reduced over, if keepdims is False
    return np.squeeze(result, axis=axis)


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Stable softmax along axis."""
    x_max = np.max(x, axis=axis, keepdims=True)
    shifted_x = x - x_max
    exp_x = np.exp(shifted_x)
    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)


def stable_softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Stable softmax along axis."""
    x_max = np.max(x, axis=axis,keepdims=True) # x_max is reduced along the specified axis
    shifted_x = x - x_max # x - x_max is broadcasted along the specified axis

    # Sum also reduces along the specified axis, so we need to keep the dimensions for broadcasting
    # This is important for the denominator to have the same shape as the numerator
    return np.exp(shifted_x) / np.sum(np.exp(shifted_x), axis=axis, keepdims=True)





def main():
    x = np.array([1000.0, 1001.0, 1002.0])
    print(softmax(x))
    print(logsumexp(x))
    print(stable_softmax(x, axis=0))


if __name__ == "__main__":
    main()
