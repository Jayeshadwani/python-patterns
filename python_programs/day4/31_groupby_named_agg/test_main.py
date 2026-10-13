import numpy as np
import pandas as pd
import pytest

from main import sales_summary

COLUMNS = ["region", "orders", "customers", "total", "avg", "largest"]


@pytest.fixture
def df():
    return pd.DataFrame({
        "region":   ["N", "N", "N", "S", "S", "E", "E", "W", "X"],
        "customer": ["c1", "c2", "c1", "c3", "c3", "c4", "c5", "c6", "c7"],
        "amount":   [100, 50, 150, 200, np.nan, np.nan, np.nan, 25, 25],
    })


def test_exact_columns_and_default_index(df):
    out = sales_summary(df)
    assert out.columns.tolist() == COLUMNS
    assert out.index.tolist() == list(range(len(out)))


def test_full_result(df):
    expected = pd.DataFrame({
        "region":    ["N", "S", "W", "X", "E"],
        "orders":    [3, 2, 1, 1, 2],
        "customers": [2, 1, 1, 1, 2],
        "total":     [300.0, 200.0, 25.0, 25.0, 0.0],
        "avg":       [100.0, 200.0, 25.0, 25.0, np.nan],
        "largest":   [150.0, 200.0, 25.0, 25.0, np.nan],
    })
    pd.testing.assert_frame_equal(sales_summary(df), expected, check_dtype=False)


def test_orders_counts_rows_including_missing_amounts(df):
    out = sales_summary(df).set_index("region")
    assert out.loc["E", "orders"] == 2
    assert out.loc["S", "orders"] == 2


def test_ties_broken_by_region_ascending(df):
    regions = sales_summary(df)["region"].tolist()
    assert regions.index("W") < regions.index("X")


def test_input_not_modified(df):
    before = df.copy()
    sales_summary(df)
    pd.testing.assert_frame_equal(df, before)


def test_single_group():
    d = pd.DataFrame({"region": ["N", "N"], "customer": ["a", "a"], "amount": [1.0, 3.0]})
    out = sales_summary(d)
    assert out.iloc[0].tolist() == ["N", 2, 1, 4.0, 2.0, 3.0]
