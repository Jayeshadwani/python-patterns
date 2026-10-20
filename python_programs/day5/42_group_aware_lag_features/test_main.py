import numpy as np
import pandas as pd

from main import add_lag_features

nan = np.nan


def make():
    rows = [
        ("B", "2026-10-01 01:00", 90.0),
        ("A", "2026-10-01 02:00", 35.0),
        ("A", "2026-10-01 00:00", 10.0),
        ("B", "2026-10-01 00:00", 100.0),
        ("A", "2026-10-01 01:00", 20.0),
    ]
    df = pd.DataFrame(rows, columns=["site", "ts", "value"])
    df["ts"] = pd.to_datetime(df["ts"])
    return df


def close(a, b):
    np.testing.assert_allclose(np.asarray(a, dtype=float), b, equal_nan=True)


def test_sorted_clean_index_and_columns():
    out = add_lag_features(make())
    assert list(out["site"]) == ["A", "A", "A", "B", "B"]
    assert list(out.index) == [0, 1, 2, 3, 4]
    assert {"site", "ts", "value", "lag1", "lag2", "delta"} <= set(out.columns)


def test_lag1_no_cross_site_leak():
    out = add_lag_features(make())
    close(out["lag1"], [nan, 10, 20, nan, 100])


def test_lag2():
    out = add_lag_features(make())
    close(out["lag2"], [nan, nan, 10, nan, nan])


def test_delta():
    out = add_lag_features(make())
    close(out["delta"], [nan, 10, 15, nan, -10])


def test_input_not_mutated():
    df = make()
    before = df.copy()
    add_lag_features(df)
    pd.testing.assert_frame_equal(df, before)
