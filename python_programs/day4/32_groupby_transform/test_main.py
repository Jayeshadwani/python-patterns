import numpy as np
import pandas as pd
import pytest

from main import group_size, share_of_group_total, zscore_within_group


@pytest.fixture
def df():
    return pd.DataFrame(
        {"g": ["a", "b", "a", "b", "a", "c"],
         "v": [2.0, 10.0, 4.0, 30.0, 6.0, 7.0]},
        index=[5, 3, 9, 1, 7, 2],
    )


def test_zscore_values_population_std(df):
    z = zscore_within_group(df, "g", "v")
    r = 2 / np.sqrt(8 / 3)
    assert z.tolist() == pytest.approx([-r, -1.0, 0.0, 1.0, r, 0.0])


def test_zscore_keeps_index_and_order(df):
    z = zscore_within_group(df, "g", "v")
    assert z.index.equals(df.index)


def test_zscore_missing_stays_missing():
    d = pd.DataFrame({"g": ["x", "x", "x"], "v": [1.0, 3.0, np.nan]})
    z = zscore_within_group(d, "g", "v").tolist()
    assert z[:2] == pytest.approx([-1.0, 1.0])
    assert np.isnan(z[2])


def test_share_of_group_total(df):
    s = share_of_group_total(df, "g", "v")
    assert s.index.equals(df.index)
    assert s.tolist() == pytest.approx([1 / 6, 0.25, 1 / 3, 0.75, 0.5, 1.0])


def test_shares_sum_to_one_per_group(df):
    s = share_of_group_total(df, "g", "v")
    assert s.groupby(df["g"]).sum().tolist() == pytest.approx([1.0, 1.0, 1.0])


def test_group_size(df):
    s = group_size(df, "g")
    assert s.index.equals(df.index)
    assert s.tolist() == [3, 2, 3, 2, 3, 1]


def test_inputs_not_modified(df):
    before = df.copy()
    zscore_within_group(df, "g", "v")
    share_of_group_total(df, "g", "v")
    group_size(df, "g")
    pd.testing.assert_frame_equal(df, before)
