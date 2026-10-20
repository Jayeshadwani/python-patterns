import pandas as pd


def add_window_features(df: pd.DataFrame) -> pd.DataFrame:
    """See problem.md."""
    # Return a copy of df containing:
    df_copy = df.copy()
    # roll3
    df_copy["roll3"] = df.rolling(3).mean()
    # roll7d
    df_copy["roll7d"] = df.rolling("7D").mean()
    # exp_mean
    df_copy["exp_mean"] = df.expanding().mean()
    # roll3_prev
    df_copy["roll3_prev"] = df.shift(1).rolling(3).mean()


    return df_copy


