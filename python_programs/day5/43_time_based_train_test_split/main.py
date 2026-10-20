import pandas as pd


def time_split(df: pd.DataFrame, cutoff, gap: str = "0D"):
    """See problem.md. Return (train, test)."""

    # 1. Convert cutoff into a pd.Timestamp
    cutoff_ts = pd.Timestamp(cutoff)

    # 2. Ensure cutoff is timezone-aware
    #    If naive, interpret it as UTC
    if cutoff_ts.tzinfo is None:
        cutoff_ts = cutoff_ts.tz_localize("UTC")
    else:
        cutoff_ts = cutoff_ts.tz_convert("UTC")
    

    # 3. Convert gap into a pd.Timedelta
    gap_td = pd.Timedelta(gap)

    # 4. Sort df by its DatetimeIndex
    df_copy = df.copy().sort_index()

    # 5. Extract train rows:
    #    index < cutoff - gap
    train_df = df_copy.loc[df_copy.index < cutoff_ts - gap_td]

    # 6. Extract test rows:
    #    index >= cutoff
    test_df = df_copy.loc[df_copy.index >= cutoff_ts]

    # 7. Raise ValueError if train or test is empty
    if train_df.empty or test_df.empty:
        raise ValueError("Train or test set is empty")

    # 8. Return train, test

    return train_df, test_df


    
if __name__ == "__main__":
    idx = pd.date_range("2026-01-01", periods=10, freq="1D", tz="UTC")
    df = pd.DataFrame({"x": range(10)}, index=idx)
    df = df.sample(frac=1.0, random_state=0)

    res = time_split(df,cutoff="2026-01-07",gap="2D")

    print(res)