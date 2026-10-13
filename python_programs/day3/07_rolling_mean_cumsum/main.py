import numpy as np
import pandas as pd


def rolling_mean(x: np.ndarray, w: int) -> np.ndarray:
    """Return the mean of every length-w window of x."""
    return pd.Series(x).rolling(w).mean().to_numpy()



def main():
    print(rolling_mean(np.array([1.0, 2, 3, 4, 5]), 2))


if __name__ == "__main__":
    main()
