import pandas as pd


def load_events(df: pd.DataFrame) -> pd.DataFrame:
    """See problem.md. Return a new DataFrame; do not mutate df."""

    # The index is **sorted ascending** and **unique** in the instants.
    # rows whose `ts` cannot be parsed are **dropped**.
    # Columns are exactly `["site", "value"]` (the `ts` column is gone).
    # The index is a `DatetimeIndex` named `"ts"`, **tz-aware in `America/New_York`**

    # Drop the rows where ts is not valid
    df_copy = df.copy().reset_index(drop=True)

    df_copy["ts"] = pd.to_datetime(df["ts"],errors="coerce",utc=True).dt.tz_convert("America/New_York")

    # df_copy["ts"].dropna(inplace=True) # calling dropna() on the series doesn't have an impact on dataframe
    df_copy.dropna(subset=["ts"],inplace=True)

    # check for duplicates in index, if any drop it (keep the first)
    df_copy.drop_duplicates(subset=["ts"],inplace=True,keep="first")


    # sort the new dataframe by index in ascending order 
    df_copy.set_index(df_copy["ts"],inplace=True)
    df_copy.sort_index(ascending=True,inplace=True)



    # make a new dataframe with existing valid rows
    return df_copy.drop(columns=["ts"],axis=1)


    


   
    
    
    


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "ts": [
                "2026-11-01T06:30:00Z",  # 01:30 EST (-05:00), second 01:30
                "2026-11-01T05:30:00Z",  # 01:30 EDT (-04:00), first 01:30
                "garbage",
                "2026-10-31T12:00:00Z",  # 08:00 EDT
                None,
            ],
            "site": ["B", "A", "X", "C", "Y"],
            "value": [3.0, 2.0, 99.0, 1.0, 98.0],
        }
    )
    print(load_events(df))