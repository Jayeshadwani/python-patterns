import numpy as np
import pandas as pd

from main import fill_short_gaps

nan = np.nan


def test_regular_series_gap_rules():
    idx = pd.date_range("2026-10-01", periods=12, freq="1h")
    s = pd.Series([nan, 1, nan, 3, nan, nan, 6, nan, nan, nan, 10, nan], index=idx, name="v")
    out = fill_short_gaps(s, max_gap=2)
    expected = [nan, 1, 2, 3, 4, 5, 6, nan, nan, nan, 10, nan]
    np.testing.assert_allclose(out.to_numpy(), expected, equal_nan=True)


def test_time_weighted_not_row_weighted():
    idx = pd.DatetimeIndex(["2026-10-01 00:00", "2026-10-01 01:00", "2026-10-01 04:00"])
    s = pd.Series([0.0, nan, 3.0], index=idx)
    out = fill_short_gaps(s, max_gap=1)
    assert out.iloc[1] == 0.75  # 1h of 4h between 0 and 3


def test_max_gap_zero_unchanged():
    idx = pd.date_range("2026-10-01", periods=4, freq="1h")
    s = pd.Series([1.0, nan, 3.0, nan], index=idx)
    out = fill_short_gaps(s, max_gap=0)
    pd.testing.assert_series_equal(out, s)


def test_long_gap_all_or_nothing():
    idx = pd.date_range("2026-10-01", periods=6, freq="1h")
    s = pd.Series([1.0, nan, nan, nan, nan, 6.0], index=idx)
    out = fill_short_gaps(s, max_gap=3)
    assert out.isna().sum() == 4  # gap of 4 > 3, left fully NaN


def test_input_not_mutated_and_metadata_kept():
    idx = pd.date_range("2026-10-01", periods=3, freq="1h")
    s = pd.Series([1.0, nan, 3.0], index=idx, name="temp")
    before = s.copy()
    out = fill_short_gaps(s, max_gap=1)
    pd.testing.assert_series_equal(s, before)
    assert out.name == "temp"
    assert out.index.equals(s.index)
