import time

import numpy as np
import pandas as pd

from main import cohort_retention, price_with_tax_fast, price_with_tax_slow

nan = np.nan


def make_orders():
    rows = [
        ("u1", "2026-01-05"), ("u1", "2026-01-06"), ("u1", "2026-02-10"), ("u1", "2026-04-03"),
        ("u2", "2026-01-20"),
        ("u3", "2026-02-02"), ("u3", "2026-03-15"),
        ("u4", "2026-02-28"), ("u4", "2026-03-01"), ("u4", "2026-04-01"),
    ]
    df = pd.DataFrame(rows, columns=["user_id", "order_ts"])
    df["order_ts"] = pd.to_datetime(df["order_ts"])
    return df


def test_cohort_shape_labels():
    out = cohort_retention(make_orders())
    assert list(out.index) == ["2026-01", "2026-02"]
    assert list(out.columns) == [0, 1, 2, 3]
    assert out.index.name == "cohort" and out.columns.name == "period"


def test_cohort_values():
    out = cohort_retention(make_orders())
    expected = np.array(
        [
            [1.0, 0.5, 0.0, 0.5],  # Jan cohort: u1,u2
            [1.0, 1.0, 0.5, nan],  # Feb cohort: u3,u4; period 3 not happened yet
        ]
    )
    np.testing.assert_allclose(out.to_numpy(dtype=float), expected, equal_nan=True)


def test_cohort_input_not_mutated():
    df = make_orders()
    before = df.copy()
    cohort_retention(df)
    pd.testing.assert_frame_equal(df, before)


def make_prices(n=200, seed=0):
    rng = np.random.default_rng(seed)
    return pd.DataFrame(
        {
            "price": rng.uniform(1, 100, n),
            "qty": rng.integers(1, 20, n),
            "category": rng.choice(["food", "toys", "tools"], n),
        },
        index=pd.RangeIndex(1000, 1000 + n),
    )


def test_fast_matches_slow():
    df = make_prices()
    slow = price_with_tax_slow(df)
    fast = price_with_tax_fast(df)
    assert fast.index.equals(slow.index)
    np.testing.assert_allclose(fast.to_numpy(), slow.to_numpy(), rtol=1e-9)


def test_qty_boundary():
    df = pd.DataFrame(
        {"price": [10.0, 10.0], "qty": [9, 10], "category": ["food", "food"]}
    )
    fast = price_with_tax_fast(df)
    np.testing.assert_allclose(fast.to_numpy(), [90 * 1.05, 100 * 0.9 * 1.05])


def test_fast_is_actually_faster():
    df = make_prices(n=30000, seed=1)
    t0 = time.perf_counter(); price_with_tax_slow(df); slow = time.perf_counter() - t0
    t0 = time.perf_counter(); price_with_tax_fast(df); fast = time.perf_counter() - t0
    assert fast * 5 < slow
