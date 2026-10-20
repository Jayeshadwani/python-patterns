import pandas as pd


def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """See problem.md."""
    # Return a **new** DataFrame, sorted by `site` then `ts`, with a clean `RangeIndex`, containing the original columns plus:
    df_copy = df.copy()

    df_copy = df_copy.sort_values(by=["site","ts"])

    # 3 new columns, lag1, lag2, and delta

    df_copy["lag1"] = df_copy.groupby("site")["value"].transform(lambda g: g.shift(1))
    df_copy["lag2"] = df_copy.groupby("site")["value"].transform(lambda g: g.shift(2))
    df_copy["delta"] = df_copy.groupby("site")["value"].transform(lambda g: g.diff())


    return df_copy.reset_index()



if __name__ == "__main__":
    rows = [
        ("B", "2026-10-01 01:00", 90.0),
        ("A", "2026-10-01 02:00", 35.0),
        ("A", "2026-10-01 00:00", 10.0),
        ("B", "2026-10-01 00:00", 100.0),
        ("A", "2026-10-01 01:00", 20.0),
    ]
    df = pd.DataFrame(rows, columns=["site", "ts", "value"])
    df["ts"] = pd.to_datetime(df["ts"])
    
    res = add_lag_features(df)

    print(res)


