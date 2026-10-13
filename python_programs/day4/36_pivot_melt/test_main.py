import numpy as np
import pandas as pd
import pytest

from main import long_to_wide, monthly_totals, wide_to_long


@pytest.fixture
def wide():
    return pd.DataFrame({"student": ["Ben", "Ana"],
                         "math": [70.0, 90.0],
                         "physics": [np.nan, 80.0],
                         "chem": [60.0, np.nan]})


def test_wide_to_long(wide):
    out = wide_to_long(wide)
    expected = pd.DataFrame({
        "student": ["Ana", "Ana", "Ben", "Ben"],
        "subject": ["math", "physics", "chem", "math"],
        "score":   [90.0, 80.0, 60.0, 70.0],
    })
    pd.testing.assert_frame_equal(out, expected, check_dtype=False)


def test_long_to_wide_with_duplicates_and_gaps():
    long = pd.DataFrame({
        "student": ["Ana", "Ana", "Ana", "Ben"],
        "subject": ["math", "math", "physics", "chem"],
        "score":   [90.0, 70.0, 80.0, 60.0],
    })
    out = long_to_wide(long)
    expected = pd.DataFrame({
        "student": ["Ana", "Ben"],
        "chem":    [np.nan, 60.0],
        "math":    [80.0, np.nan],
        "physics": [80.0, np.nan],
    })
    pd.testing.assert_frame_equal(out, expected, check_dtype=False)
    assert out.columns.name is None


def test_round_trip(wide):
    back = long_to_wide(wide_to_long(wide))
    original = wide[["student", "chem", "math", "physics"]].sort_values("student").reset_index(drop=True)
    pd.testing.assert_frame_equal(back, original, check_dtype=False)


@pytest.fixture
def sales():
    return pd.DataFrame({
        "date":   ["2024-01-05", "2024-01-20", "2024-01-10", "2024-03-02"],
        "region": ["N", "N", "S", "S"],
        "amount": [100, 50, 30, 70],
    })


def test_monthly_totals_fills_empty_month(sales):
    out = monthly_totals(sales)
    expected = pd.DataFrame({
        "month": ["2024-01", "2024-02", "2024-03"],
        "N": [150, 0, 0],
        "S": [30, 0, 70],
    })
    pd.testing.assert_frame_equal(out, expected, check_dtype=False)
    assert out.columns.name is None


def test_monthly_totals_year_boundary():
    d = pd.DataFrame({"date": ["2023-12-31", "2024-02-01"],
                      "region": ["B", "A"], "amount": [5, 7]})
    out = monthly_totals(d)
    assert out["month"].tolist() == ["2023-12", "2024-01", "2024-02"]
    assert out.columns.tolist() == ["month", "A", "B"]
    assert out["A"].tolist() == [0, 0, 7]
    assert out["B"].tolist() == [5, 0, 0]


def test_inputs_not_modified(wide, sales):
    w0, s0 = wide.copy(), sales.copy()
    wide_to_long(wide)
    monthly_totals(sales)
    pd.testing.assert_frame_equal(wide, w0)
    pd.testing.assert_frame_equal(sales, s0)
