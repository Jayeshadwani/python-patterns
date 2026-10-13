import numpy as np
import pandas as pd
import pytest

from main import checked_merge, duplicate_keys, row_growth


@pytest.fixture
def orders():
    return pd.DataFrame({"order_id": [1, 2, 3, 4], "customer_id": [1, 2, 2, 3]})


@pytest.fixture
def clean():
    return pd.DataFrame({"customer_id": [1, 2, 3], "name": ["Ana", "Ben", "Cy"]})


@pytest.fixture
def dirty():
    return pd.DataFrame({"customer_id": [1, 2, 3, 2],
                         "name": ["Ana", "Ben", "Cy", "Ben (old)"]})


def test_duplicate_keys(dirty):
    assert duplicate_keys(dirty, "customer_id") == [2]


def test_duplicate_keys_sorted_and_ignores_missing():
    d = pd.DataFrame({"k": [5, 3, 5, 3, np.nan, np.nan, 1]})
    assert duplicate_keys(d, "k") == [3.0, 5.0]


def test_duplicate_keys_none(clean):
    assert duplicate_keys(clean, "customer_id") == []


def test_row_growth(orders, clean, dirty):
    assert row_growth(orders, clean, "customer_id") == 1.0
    assert row_growth(orders, dirty, "customer_id") == pytest.approx(1.5)


def test_row_growth_empty_left(clean):
    empty = pd.DataFrame({"customer_id": pd.Series([], dtype="int64")})
    assert row_growth(empty, clean, "customer_id") == 1.0


def test_checked_merge_valid_equals_plain_merge(orders, clean):
    out = checked_merge(orders, clean, "customer_id")
    pd.testing.assert_frame_equal(out, orders.merge(clean, on="customer_id", how="left"))


def test_checked_merge_how_is_passed_through(orders, clean):
    extra = pd.concat([clean, pd.DataFrame({"customer_id": [7], "name": ["Zed"]})],
                      ignore_index=True)
    out = checked_merge(orders, extra, "customer_id", how="right")
    assert len(out) == 5


def test_checked_merge_rejects_duplicate_right_keys(orders, dirty):
    with pytest.raises(ValueError) as e:
        checked_merge(orders, dirty, "customer_id")
    msg = str(e.value)
    assert "many_to_one" in msg
    assert "right=[2]" in msg
    assert "left=[2]" in msg


def test_one_to_one_reports_left_side(orders, clean):
    with pytest.raises(ValueError) as e:
        checked_merge(orders, clean, "customer_id", validate="one_to_one")
    msg = str(e.value)
    assert "one_to_one" in msg
    assert "left=[2]" in msg
    assert "right=[]" in msg


def test_inputs_not_modified(orders, dirty):
    o0, d0 = orders.copy(), dirty.copy()
    with pytest.raises(ValueError):
        checked_merge(orders, dirty, "customer_id")
    pd.testing.assert_frame_equal(orders, o0)
    pd.testing.assert_frame_equal(dirty, d0)
