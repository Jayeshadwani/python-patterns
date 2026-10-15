import numpy as np
import pandas as pd

from main import hourly_stats


def make(times, values):
    idx = pd.DatetimeIndex(pd.to_datetime(times, utc=True))
    return pd.DataFrame({"value": values}, index=idx)


def test_gap_hour_present_with_count_zero():
    df = make(
        ["2026-10-01 00:10", "2026-10-01 00:50", "2026-10-01 02:30", "2026-10-01 02:40"],
        [1.0, 3.0, 10.0, np.nan],
    )
    out = hourly_stats(df)
    expected_idx = pd.date_range("2026-10-01 00:00", periods=3, freq="1h", tz="UTC")
    assert list(out.index) == list(expected_idx)
    assert list(out.columns) == ["mean", "max", "count"]
    np.testing.assert_allclose(out["mean"], [2.0, np.nan, 10.0], equal_nan=True)
    np.testing.assert_allclose(out["max"], [3.0, np.nan, 10.0], equal_nan=True)
    assert list(out["count"]) == [2, 0, 1]


def test_bin_edges_left_closed():
    df = make(["2026-10-01 00:59:59", "2026-10-01 01:00:00"], [1.0, 2.0])
    out = hourly_stats(df)
    assert list(out["count"]) == [1, 1]
    assert list(out["mean"]) == [1.0, 2.0]


def test_unsorted_input():
    df = make(["2026-10-01 02:30", "2026-10-01 00:10"], [10.0, 1.0])
    out = hourly_stats(df)
    assert len(out) == 3
    assert out.index.is_monotonic_increasing
    assert list(out["count"]) == [1, 0, 1]


def test_tz_kept_utc():
    df = make(["2026-10-01 00:10"], [1.0])
    out = hourly_stats(df)
    assert str(out.index.tz) == "UTC"
