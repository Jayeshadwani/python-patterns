import numpy as np
import pandas as pd
import pytest

from main import nth_highest_per_group, top_n_per_group


@pytest.fixture
def emp():
    return pd.DataFrame({
        "dept":   ["Eng", "Eng", "Eng", "Eng", "Ops", "Ops", "Ops", "HR"],
        "name":   ["Ana", "Ben", "Cy", "Di", "Eve", "Fay", "Gus", "Hal"],
        "salary": [120, 100, 120, 90, 80, 80, np.nan, 70],
    }, index=[8, 7, 6, 5, 4, 3, 2, 1])


def test_top_2_rows(emp):
    out = top_n_per_group(emp, "dept", "salary", 2)
    assert out["name"].tolist() == ["Ana", "Cy", "Hal", "Eve", "Fay"]
    assert out["dept"].tolist() == ["Eng", "Eng", "HR", "Ops", "Ops"]


def test_top_n_keeps_all_columns_and_resets_index(emp):
    out = top_n_per_group(emp, "dept", "salary", 2)
    assert out.columns.tolist() == ["dept", "name", "salary"]
    assert out.index.tolist() == list(range(len(out)))


def test_top_1_ties_keep_original_order(emp):
    out = top_n_per_group(emp, "dept", "salary", 1)
    assert out["name"].tolist() == ["Ana", "Hal", "Eve"]


def test_top_n_larger_than_group(emp):
    out = top_n_per_group(emp, "dept", "salary", 10)
    assert len(out) == 7          # the NaN row is ignored
    assert "Gus" not in out["name"].tolist()


def test_nth_highest_2(emp):
    out = nth_highest_per_group(emp, "dept", "salary", 2)
    expected = pd.DataFrame({"dept": ["Eng"], "salary": [100.0]})
    pd.testing.assert_frame_equal(out, expected, check_dtype=False)


def test_nth_highest_1_and_3(emp):
    one = nth_highest_per_group(emp, "dept", "salary", 1)
    assert one["dept"].tolist() == ["Eng", "HR", "Ops"]
    assert one["salary"].tolist() == [120, 70, 80]
    three = nth_highest_per_group(emp, "dept", "salary", 3)
    assert three["dept"].tolist() == ["Eng"]
    assert three["salary"].tolist() == [90]


def test_nth_highest_nothing_qualifies(emp):
    out = nth_highest_per_group(emp, "dept", "salary", 4)
    assert len(out) == 0
    assert out.columns.tolist() == ["dept", "salary"]


@pytest.mark.parametrize("fn", [top_n_per_group, nth_highest_per_group])
def test_invalid_n(emp, fn):
    with pytest.raises(ValueError):
        fn(emp, "dept", "salary", 0)


def test_input_not_modified(emp):
    before = emp.copy()
    top_n_per_group(emp, "dept", "salary", 2)
    nth_highest_per_group(emp, "dept", "salary", 2)
    pd.testing.assert_frame_equal(emp, before)
