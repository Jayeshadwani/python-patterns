import numpy as np
import pandas as pd
from pandas.tseries.offsets import DateOffset


def cohort_retention(orders: pd.DataFrame) -> pd.DataFrame:
    """Part A. See problem.md."""

    # Stages:
    # 1. Extract month from order_ts & store in order_month
    df = orders.copy()
    df["order_ts"] = pd.to_datetime(df["order_ts"])
    df["order_month"] = df["order_ts"].dt.strftime("%Y-%m")

    # 2. Create column first_order_month from grouping by user_id
    df["first_order_month"] = df.groupby("user_id")["order_month"].transform(
        lambda s: s.sort_values().iloc[0]
    )

    # 3. Get user_ids from grouping by first_order_month (x)
    first_order_month_userids_dict = (
        df.groupby("first_order_month")
        .apply(lambda g: g.drop_duplicates(subset=["user_id"])["user_id"].to_list())
        .to_dict()
    )

    # print(first_order_month_userids_dict)

    # 4. Get user_ids from grouping by order_month (y)
    order_month_userids_dict = (
        df.groupby("order_month")
        .apply(lambda g: g.drop_duplicates(subset=["user_id"])["user_id"].to_list())
        .to_dict()
    )

    # print(order_month_userids_dict)

    # 5. From start of order_month to recent order_month count periods
    end = pd.Timestamp(df["order_month"].max())
    start = pd.Timestamp(df["order_month"].min())

    periods = (end.year - start.year) * 12 + (end.month - start.month)
    # print(periods)

    # 6. For each period and cohort_month calculate retention_rate
    retention_rate = {}

    for cohort_month in first_order_month_userids_dict.keys():
        for i in range(1, periods + 1):
            # add a month to timestamp
            y = (pd.Timestamp(cohort_month) + DateOffset(months=i)).strftime("%Y-%m")

            user_ids_in_y = order_month_userids_dict.get(y, [])
            user_ids_in_x = first_order_month_userids_dict.get(cohort_month)

            # print(user_ids_in_y, user_ids_in_x, i, cohort_month)

            # intersection of two python list
            intrsctn_count = len(set(user_ids_in_y) & set(user_ids_in_x))
            all_count = len(user_ids_in_x)

            rr = round((intrsctn_count / all_count), 2)

            if y > pd.Timestamp(end).strftime("%Y-%m"):
                rr = np.nan

            # python list setdefault()
            retention_rate.setdefault(cohort_month, [1.0]).append(rr)

    df = pd.DataFrame.from_dict(retention_rate, orient="index")

    df.index.name = "cohort"
    df.columns.name = "period"

    return df


def price_with_tax_slow(df: pd.DataFrame) -> pd.Series:
    """Given. Slow reference implementation, do not edit."""

    def row(r):
        base = r["price"] * r["qty"]
        if r["qty"] >= 10:
            base *= 0.9
        rate = 0.05 if r["category"] == "food" else 0.18
        return base * (1 + rate)

    return df.apply(row, axis=1)


def price_with_tax_fast(df: pd.DataFrame) -> pd.Series:
    """Part B. Same result as price_with_tax_slow, vectorized."""

    # Hey GPT, how do you vectorize a Python function – custom column operations works best in pandas

    base = np.where(
        df["qty"] >= 10, df["price"] * df["qty"] * 0.9, df["price"] * df["qty"]
    )
    rate = np.where(df["category"] == "food", 0.05, 0.18)

    return pd.Series(base * (1 + rate), index=df.index)


if __name__ == "__main__":
    rows = [
        ("u1", "2026-01-05"),
        ("u1", "2026-01-06"),
        ("u2", "2026-01-20"),
        ("u1", "2026-02-10"),
        ("u3", "2026-02-02"),
        ("u4", "2026-02-28"),
        ("u3", "2026-03-15"),
        ("u4", "2026-03-01"),
        ("u1", "2026-04-03"),
        ("u4", "2026-04-01"),
    ]
    df = pd.DataFrame(rows, columns=["user_id", "order_ts"])
    df["order_ts"] = pd.to_datetime(df["order_ts"])
    print(cohort_retention(df))

    ####

    rng = np.random.default_rng(1)
    df2 = pd.DataFrame(
        {
            "price": rng.uniform(1, 100, 200),
            "qty": rng.integers(1, 20, 200),
            "category": rng.choice(["food", "toys", "tools"], 200),
        },
        index=pd.RangeIndex(1000, 1000 + 200),
    )

    print(price_with_tax_fast(df2))
