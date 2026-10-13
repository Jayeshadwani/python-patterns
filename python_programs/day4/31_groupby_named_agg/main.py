import pandas as pd


def sales_summary(df: pd.DataFrame) -> pd.DataFrame:
    """One row per region: region, orders, customers, total, avg, largest."""
    grouped_res = df.groupby("region").agg(total=("amount","sum"),avg=("amount","mean"),largest=("amount","max"),orders=("customer","count"),customers=("customer","nunique"))

    # print(pd.concat([df,grouped_res])) # this stacks the df vertically axis=0
    
    return grouped_res.reset_index()[["region", "orders", "customers", "total", "avg", "largest"]]


def main():
    df = pd.DataFrame({"region": ["N", "N", "S"],
                       "customer": ["c1", "c2", "c3"],
                       "amount": [100, 50, None]})
    print(sales_summary(df))


if __name__ == "__main__":
    main()
