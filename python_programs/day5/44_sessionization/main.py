import pandas as pd


def sessionize(df: pd.DataFrame, timeout: str = "30min") -> pd.DataFrame:
    """See problem.md."""

    # Stage 1: SORT values by user and then ts
    df_copy = df.copy().sort_values(by=["user_id", "ts"])

    # Stage 2: FIND difference between prev and next rows and store value in `session_diff` column
    df_copy["session_diff"] = df_copy["ts"].diff()

    # Stage 3: COMPARE session_diff > timeout and store in `is_same_session` column
    df_copy["is_same_session"] = df_copy["session_diff"] > pd.Timedelta(timeout)

    # Stage 4: COMPUTE is_same_session.cumsum() and store in `session_no`, (should start from 0)
    df_copy["session_no"] = df_copy.groupby("user_id")["is_same_session"].transform(
        "cumsum"
    )

    # Stage 5: DROP the `session_diff` & `is_same_session` columns
    return df_copy.drop(columns=["session_diff", "is_same_session"]).reset_index()


if __name__ == "__main__":
    rows = [
        ("u2", "2026-10-01 09:31"),
        ("u1", "2026-10-01 11:30"),
        ("u1", "2026-10-01 10:00"),
        ("u2", "2026-10-01 09:00"),
        ("u1", "2026-10-01 10:40"),
        ("u1", "2026-10-01 10:10"),
    ]
    df = pd.DataFrame(rows, columns=["user_id", "ts"])
    df["ts"] = pd.to_datetime(df["ts"])

    print(sessionize(df))
