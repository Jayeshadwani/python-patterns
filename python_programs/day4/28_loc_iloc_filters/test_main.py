import pandas as pd
import pytest

from main import by_labels, filter_city_age, first_n, last_row_name


@pytest.fixture
def df():
    return pd.DataFrame(
        {"name": ["Ana", "Ben", "Cleo", "Dev"],
         "age": [34, 19, 41, 27],
         "city": ["Pune", "Delhi", "Pune", "Pune"]},
        index=[30, 10, 20, 40],
    )


def test_first_n_is_positional(df):
    out = first_n(df, 2)
    assert isinstance(out, pd.DataFrame)
    assert out.index.tolist() == [30, 10]
    assert out["name"].tolist() == ["Ana", "Ben"]


def test_first_n_edges(df):
    assert len(first_n(df, 0)) == 0
    assert first_n(df, 10).index.tolist() == [30, 10, 20, 40]


def test_by_labels_uses_labels_in_given_order(df):
    out = by_labels(df, [40, 10])
    assert isinstance(out, pd.DataFrame)
    assert out.index.tolist() == [40, 10]
    assert out["name"].tolist() == ["Dev", "Ben"]


def test_by_labels_missing_label_raises(df):
    with pytest.raises(KeyError):
        by_labels(df, [10, 99])


def test_by_labels_empty_list(df):
    assert len(by_labels(df, [])) == 0


def test_filter_city_age(df):
    out = filter_city_age(df, "Pune", 30)
    assert out.columns.tolist() == ["name", "age"]
    assert out.index.tolist() == [30, 20]
    assert out["age"].tolist() == [34, 41]


def test_filter_boundary_is_inclusive(df):
    assert filter_city_age(df, "Pune", 27).index.tolist() == [30, 20, 40]


def test_filter_no_match_keeps_columns(df):
    out = filter_city_age(df, "Goa", 0)
    assert len(out) == 0
    assert out.columns.tolist() == ["name", "age"]


def test_last_row_name_is_positional(df):
    assert last_row_name(df) == "Dev"


def test_last_row_name_default_index():
    d = pd.DataFrame({"name": ["a", "b", "c"]})
    assert last_row_name(d) == "c"


def test_input_not_modified(df):
    before = df.copy()
    first_n(df, 2)
    by_labels(df, [10])
    filter_city_age(df, "Pune", 30)
    last_row_name(df)
    pd.testing.assert_frame_equal(df, before)
