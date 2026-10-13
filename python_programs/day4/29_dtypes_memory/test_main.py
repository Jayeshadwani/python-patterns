import numpy as np
import pandas as pd
import pytest

from main import shrink


@pytest.fixture
def df():
    n = 1000
    i = np.arange(n)
    return pd.DataFrame({
        "city": pd.Series(["Pune", "Delhi", "Mumbai", "Pune"] * 250, dtype="object"),
        "user_id": pd.Series([f"user_{k}" for k in range(n)], dtype="object"),
        "age": (i % 90).astype("int64"),
        "big": (i * 1_000_000).astype("int64"),
        "score": np.where(i % 10 == 0, np.nan, (i % 8) * 0.25),
        "flag": i % 2 == 0,
    })


def is_cat(s):
    return isinstance(s.dtype, pd.CategoricalDtype)


def test_low_cardinality_text_becomes_category(df):
    assert is_cat(shrink(df)["city"])


def test_high_cardinality_text_stays_text(df):
    assert not is_cat(shrink(df)["user_id"])


def test_integers_downcast_to_smallest_fit(df):
    out = shrink(df)
    assert out["age"].dtype == np.dtype("int8")
    assert out["big"].dtype == np.dtype("int32")


def test_floats_become_float32_and_nan_kept(df):
    out = shrink(df)
    assert out["score"].dtype == np.dtype("float32")
    assert out["score"].isna().sum() == df["score"].isna().sum()


def test_bool_untouched(df):
    assert shrink(df)["flag"].dtype == np.dtype("bool")


def test_values_columns_and_index_unchanged(df):
    out = shrink(df)
    assert out.columns.tolist() == df.columns.tolist()
    assert out.index.equals(df.index)
    for c in ["age", "big", "score"]:
        pd.testing.assert_series_equal(out[c].astype(df[c].dtype), df[c])
    assert out["city"].astype("object").tolist() == df["city"].tolist()
    assert out["user_id"].astype("object").tolist() == df["user_id"].tolist()


def test_memory_goes_down(df):
    out = shrink(df)
    assert out.memory_usage(deep=True).sum() < df.memory_usage(deep=True).sum()
    assert out["city"].memory_usage(deep=True) < 0.1 * df["city"].memory_usage(deep=True)


def test_input_not_modified(df):
    before = df.dtypes.copy()
    shrink(df)
    assert df.dtypes.equals(before)


def test_threshold_controls_category(df):
    assert not is_cat(shrink(df, cat_threshold=0.0)["city"])
    assert is_cat(shrink(df, cat_threshold=1.1)["user_id"])


def test_threshold_is_strict(df):
    # city has 3 unique values in 1000 rows: ratio is exactly 3/1000 = 0.003
    assert not is_cat(shrink(df, cat_threshold=0.003)["city"])
    assert is_cat(shrink(df, cat_threshold=0.0031)["city"])


def test_empty_frame_does_not_raise(df):
    out = shrink(df.iloc[0:0])
    assert len(out) == 0
    assert out.columns.tolist() == df.columns.tolist()
