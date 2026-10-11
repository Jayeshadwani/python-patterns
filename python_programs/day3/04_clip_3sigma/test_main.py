import numpy as np
from main import clip_3sigma


def make():
    x = np.random.default_rng(3).normal(size=1000)
    x[0], x[1] = 100.0, -100.0
    return x


def test_matches_reference():
    x = make()
    mu, sd = x.mean(), x.std()
    assert np.allclose(clip_3sigma(x), np.clip(x, mu - 3 * sd, mu + 3 * sd))


def test_high_outlier_is_clipped():
    x = make()
    assert clip_3sigma(x)[0] < 100.0


def test_low_outlier_is_clipped():
    x = make()
    assert clip_3sigma(x)[1] > -100.0


def test_inliers_unchanged():
    x = make()
    inl = np.abs(x - x.mean()) <= 3 * x.std()
    assert np.array_equal(clip_3sigma(x)[inl], x[inl])


def test_input_not_modified():
    x = make()
    before = x.copy()
    clip_3sigma(x)
    assert np.array_equal(x, before)


def test_constant_array():
    x = np.full(10, 4.0)
    assert np.allclose(clip_3sigma(x), x)
