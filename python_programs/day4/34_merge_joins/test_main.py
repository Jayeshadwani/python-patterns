import numpy as np
import pandas as pd
import pytest

from main import (customers_without_orders, inner_join, left_join,
                  orders_with_unknown_customer)


@pytest.fixture
def customers():
    return pd.DataFrame({"customer_id": [4, 1, 3, 2],
                         "name": ["Dev", "Ana", "Cleo", "Ben"]})


@pytest.fixture
def orders():
    return pd.DataFrame({"order_id": [104, 102, 103, 101],
                         "customer_id": [9, 1, 3, 1],
                         "amount": [20.0, 70.0, np.nan, 50.0]})


def test_inner_join(customers, orders):
    expected = pd.DataFrame({
        "customer_id": [1, 1, 3],
        "name": ["Ana", "Ana", "Cleo"],
        "order_id": [101, 102, 103],
        "amount": [50.0, 70.0, np.nan],
    })
    pd.testing.assert_frame_equal(inner_join(customers, orders), expected, check_dtype=False)


def test_left_join_keeps_all_customers(customers, orders):
    expected = pd.DataFrame({
        "customer_id": [1, 1, 2, 3, 4],
        "name": ["Ana", "Ana", "Ben", "Cleo", "Dev"],
        "order_id": [101, 102, np.nan, 103, np.nan],
        "amount": [50.0, 70.0, np.nan, np.nan, np.nan],
    })
    pd.testing.assert_frame_equal(left_join(customers, orders), expected, check_dtype=False)


def test_customers_without_orders(customers, orders):
    out = customers_without_orders(customers, orders)
    expected = pd.DataFrame({"customer_id": [2, 4], "name": ["Ben", "Dev"]})
    pd.testing.assert_frame_equal(out, expected, check_dtype=False)


def test_customer_with_missing_amount_still_has_an_order(customers, orders):
    out = customers_without_orders(customers, orders)
    assert "Cleo" not in out["name"].tolist()


def test_orders_with_unknown_customer(customers, orders):
    out = orders_with_unknown_customer(customers, orders)
    expected = pd.DataFrame({"order_id": [104], "customer_id": [9], "amount": [20.0]})
    pd.testing.assert_frame_equal(out, expected, check_dtype=False)


def test_nothing_unmatched_gives_empty_with_columns(customers):
    ok_orders = pd.DataFrame({"order_id": [1], "customer_id": [1], "amount": [5.0]})
    out = orders_with_unknown_customer(customers, ok_orders)
    assert len(out) == 0
    assert out.columns.tolist() == ["order_id", "customer_id", "amount"]


def test_inputs_not_modified(customers, orders):
    c0, o0 = customers.copy(), orders.copy()
    inner_join(customers, orders)
    left_join(customers, orders)
    customers_without_orders(customers, orders)
    orders_with_unknown_customer(customers, orders)
    pd.testing.assert_frame_equal(customers, c0)
    pd.testing.assert_frame_equal(orders, o0)
