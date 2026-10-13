import numpy as np
import pandas as pd
import pytest

from main import fill_with_group_median, missing_report


@pytest.fixture
def df():
    return pd.DataFrame(
        {"dept": ["A", "A", "A", "B", "B", "C", "C", None],
         "salary": [10, np.nan, 30, 40, np.nan, np.nan, np.nan, np.nan],
         "name": list("pqrstuvw")},
        index=[7, 3, 5, 1, 9, 2, 4, 8],
    )


def test_missing_report_sorted_and_filtered():
    d = pd.DataFrame({"a": [1, np.nan, 3, 4],
                      "b": [np.nan, np.nan, 3, 4],
                      "c": [1, 2, 3, 4]})
    out = missing_report(d)
    assert out.index.tolist() == ["b", "a"]
    assert out.tolist() == [0.5, 0.25]


def test_missing_report_ties_keep_column_order():
    d = pd.DataFrame({"x": [1, np.nan], "y": [np.nan, 2], "z": [1, 2]})
    assert missing_report(d).index.tolist() == ["x", "y"]


def test_missing_report_nothing_missing():
    out = missing_report(pd.DataFrame({"a": [1, 2]}))
    assert len(out) == 0


def test_group_median_values(df):
    out = fill_with_group_median(df, "dept", "salary")
    assert out["salary"].tolist() == [10.0, 20.0, 30.0, 40.0, 40.0, 30.0, 30.0, 30.0]


def test_existing_values_unchanged(df):
    out = fill_with_group_median(df, "dept", "salary")
    known = df["salary"].notna()
    assert out.loc[known, "salary"].tolist() == df.loc[known, "salary"].tolist()


def test_index_and_other_columns_preserved(df):
    out = fill_with_group_median(df, "dept", "salary")
    assert out.index.equals(df.index)
    assert out["name"].tolist() == df["name"].tolist()
    assert out["dept"].tolist()[:7] == df["dept"].tolist()[:7]


def test_input_not_modified(df):
    before = df.copy()
    fill_with_group_median(df, "dept", "salary")
    pd.testing.assert_frame_equal(df, before)


def test_whole_column_missing_left_alone():
    d = pd.DataFrame({"g": ["a", "b"], "v": [np.nan, np.nan]})
    out = fill_with_group_median(d, "g", "v")
    assert out["v"].isna().all()


def test_no_missing_is_identity():
    d = pd.DataFrame({"g": ["a", "b"], "v": [1.0, 2.0]})
    pd.testing.assert_frame_equal(fill_with_group_median(d, "g", "v"), d)
