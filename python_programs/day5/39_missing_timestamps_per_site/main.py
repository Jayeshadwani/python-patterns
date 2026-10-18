import pandas as pd

# `df` has columns `site` (str), `ts` (tz-naive `datetime64`), `value`. Each site should report every `freq`. 
# For **each site separately**, find the timestamps that are missing between **that site's own first and last `ts`**.


def missing_timestamps(df: pd.DataFrame, freq: str = "15min") -> pd.DataFrame:
    """See problem.md."""

    # find missing timestamps per site

    # 1. cleaning - drop duplicates and nulls
    # 2. sorting - ascending order
    # 3. group per site - min_ts, max_ts 
    # 4. comparison with 15min freq range, (loop / subtraction)
    # 5. if missing store in resultant 

    def find_missing_ts_per_site(g):
        sorted_ts_per_site = g.drop_duplicates(subset=["ts"]).dropna(subset=["ts"]).sort_values(by="ts")

        # date format
        sorted_ts_per_site["ts"] = pd.to_datetime(sorted_ts_per_site["ts"])

        min_ts = sorted_ts_per_site["ts"].min()

        max_ts = sorted_ts_per_site["ts"].max()


        # create index with all 15min freq from min_ts to max_ts
        all_freq = pd.date_range(start=min_ts,end=max_ts,freq=freq)

        #mising_freq = all_freq - sorted_ts_per_site["ts"] # unequal length

        mising_freq = all_freq[~all_freq.isin(sorted_ts_per_site["ts"])]

        return pd.DataFrame({"site": g["site"].iloc[0], "ts":mising_freq})


    missing_freq_per_site = df.groupby("site",group_keys=False).apply(find_missing_ts_per_site).reset_index(drop=True)

    #print(type(missing_freq_per_site))

    return missing_freq_per_site


    



if __name__ == "__main__":
    rows = [
        # site A: missing 00:30 (00:15 duplicated)
        ("A", "2026-10-01 00:00"), ("A", "2026-10-01 00:15"), ("A", "2026-10-01 00:15"),
        ("A", "2026-10-01 00:45"), ("A", "2026-10-01 01:00"),
        # site B: missing 00:45, 01:00, 01:15
        ("B", "2026-10-01 00:30"), ("B", "2026-10-01 00:15"), ("B", "2026-10-01 00:00"),
        ("B", "2026-10-01 01:30"),
        # site C: single row
        ("C", "2026-10-01 05:00"),
    ]
    df = pd.DataFrame(rows, columns=["site", "ts"])
    print(missing_timestamps(df))



    