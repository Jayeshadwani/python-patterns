import pandas as pd
import pytest

from main import time_split


def make():
    idx = pd.date_range("2026-01-01", periods=10, freq="1D", tz="UTC")
    df = pd.DataFrame({"x": range(10)}, index=idx)
    return df.sample(frac=1.0, random_state=0)  # shuffled on purpose


def days(df):
    return [d.day for d in df.index]


def test_split_with_gap():
    train, test = time_split(make(), "2026-01-07", gap="2D")
    assert days(train) == [1, 2, 3, 4]
    assert days(test) == [7, 8, 9, 10]


def test_no_gap_default():
    train, test = time_split(make(), "2026-01-07")
    assert days(train) == [1, 2, 3, 4, 5, 6]
    assert days(test) == [7, 8, 9, 10]


def test_timestamp_cutoff_aware():
    c = pd.Timestamp("2026-01-07", tz="UTC")
    train, test = time_split(make(), c, gap="2D")
    assert days(train) == [1, 2, 3, 4]
    assert days(test) == [7, 8, 9, 10]


def test_sorted_and_no_overlap():
    train, test = time_split(make(), "2026-01-07", gap="1D")
    assert train.index.is_monotonic_increasing and test.index.is_monotonic_increasing
    assert train.index.max() < test.index.min()
    assert str(train.index.tz) == "UTC"


def test_empty_side_raises():
    with pytest.raises(ValueError):
        time_split(make(), "2025-01-01")
    with pytest.raises(ValueError):
        time_split(make(), "2027-01-01")
