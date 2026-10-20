import numpy as np
import pandas as pd

from main import add_window_features

nan = np.nan


def make():
    idx = pd.to_datetime(
        ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-05", "2026-01-10", "2026-01-11"]
    )
    return pd.DataFrame({"value": [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]}, index=idx)


def close(a, b):
    np.testing.assert_allclose(np.asarray(a, dtype=float), b, equal_nan=True)


def test_roll3_row_based():
    out = add_window_features(make())
    close(out["roll3"], [nan, nan, 20, 30, 40, 50])


def test_roll7d_time_based():
    out = add_window_features(make())
    # Jan 10 window is (Jan 3, Jan 10] -> Jan 5, Jan 10 only
    close(out["roll7d"], [10, 15, 20, 25, 45, 50])


def test_expanding_mean():
    out = add_window_features(make())
    close(out["exp_mean"], [10, 15, 20, 25, 30, 35])


def test_roll3_prev_excludes_current():
    out = add_window_features(make())
    close(out["roll3_prev"], [nan, nan, nan, 20, 30, 40])


def test_columns_and_not_mutated():
    df = make()
    before = df.copy()
    out = add_window_features(df)
    pd.testing.assert_frame_equal(df, before)
    assert {"value", "roll3", "roll7d", "exp_mean", "roll3_prev"} <= set(out.columns)
    assert out.index.equals(df.index)
