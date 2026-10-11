import numpy as np


def clip_3sigma(x: np.ndarray) -> np.ndarray:
    """Clip values beyond mean +/- 3 standard deviations."""

    mu = x.mean()
    sd = x.std()

    x_max = mu + (3*sd)
    x_min = mu - (3*sd)

    return np.clip(x,x_min,x_max)

def main():
    x = np.random.default_rng(0).normal(size=100)
    x[0] = 50.0
    print(clip_3sigma(x)[:3])


if __name__ == "__main__":
    main()
