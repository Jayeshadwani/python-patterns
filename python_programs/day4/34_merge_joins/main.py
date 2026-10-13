import pandas as pd

def inner_join(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Customers with orders, one row per order."""
    return (
            pd.merge(customers, orders, how="inner", on="customer_id")
            .sort_values(["customer_id", "order_id"])
            .reset_index(drop=True)
        )


def left_join(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """All customers; NaN order columns where a customer has no orders."""
    # return pd.merge(customers, orders, how="left", on="customer_id") # merge does not guarantee ordering, and na_position

    return (
        pd.merge(customers, orders, how="left", on="customer_id")
        .sort_values(["customer_id", "order_id"], na_position="last")
        .reset_index(drop=True)
    )


def customers_without_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Customer rows with no matching order (anti-join)."""
    
    outer_table = pd.merge(customers, orders, how="left",on="customer_id") 

    return (outer_table.loc[outer_table["order_id"].isna(),["customer_id","name"]].sort_values(by="customer_id").reset_index(drop=True))

def orders_with_unknown_customer(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Order rows whose customer_id is not in customers (anti-join)."""
    merged_df = pd.merge(
        customers, orders, how="right", on="customer_id"
    )

    return (
        merged_df.loc[
            merged_df["name"].isna(),
            ["order_id", "customer_id", "amount"]
        ]
        .sort_values(["customer_id", "order_id"])
        .reset_index(drop=True)
    )

def main():
    customers = pd.DataFrame({"customer_id": [1, 2], "name": ["Ana", "Ben"]})
    orders = pd.DataFrame({"order_id": [101, 102], "customer_id": [1, 9], "amount": [50.0, 20.0]})
    print(customers_without_orders(customers, orders))
    print(orders_with_unknown_customer(customers, orders))


if __name__ == "__main__":
    main()
