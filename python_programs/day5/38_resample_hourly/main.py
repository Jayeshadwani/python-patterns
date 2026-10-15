import pandas as pd
import numpy as np


def hourly_stats(df: pd.DataFrame) -> pd.DataFrame:
    """See problem.md."""

    # Return a DataFrame indexed by **every hour** from the first event's hour to the last event's hour (no hour skipped), with columns exactly:
    # mean (mean of non-null `value` in that hour  ), max (max of non-null `value` in that hour ), count (number of **non-null** `value` in that hour)


    # Bins are **left-closed, left-labeled**: 00:00:00 to 00:59:59 is labeled 00:00; an event at exactly 01:00:00 belongs to hour 01.

    # find the min and max from the index, label it as first and last hour

    # recreate index from first to last hour, 
    first_hour = df.index.min().floor("h")
    last_hour = df.index.max().floor("h")

    new_idx = pd.date_range(start=first_hour,end=last_hour,freq="1h")

    index_counter = { ts : {"count": 0, "sum": 0, "mean": np.nan, "max" : np.nan} for ts in new_idx}
    #print(type(index_counter))

    for row, idx in enumerate(df.index):
        # print(df.iloc[row].values[0],">>>>>>>>>>>>>>>>>>>>>>>>>")
        # print(isinstance(df.iloc[row].values[0],(int,float)))
        ts = idx.floor("h")
        value = df.iloc[row].values[0]
        if pd.notna(value) and isinstance(value,(float)):
           
           curr = index_counter.get(ts)
           
           # update count
           curr["count"] += 1
           curr["sum"] += value
           
           # update max
           if pd.isna(curr["max"]) or value > curr["max"]:
               curr["max"] = value

           # update mean
           curr["mean"] = curr["sum"] / curr["count"]


    # return pd.DataFrame({
    #     "mean": index_counter.values
    # },
    #              index=list(index_counter))

    # orient="index" → Outer dictionary keys become row indexes.
    result = pd.DataFrame.from_dict(index_counter, orient="index")

    # Inner dictionary keys (mean, max, count) become columns.
    #  result[["mean", "max", "count"]] → Selects and orders columns.
    result = result[["mean", "max", "count"]]
    result.index.name = "ts"

    return result






if __name__ == "__main__":
    def make(times, values):
        idx = pd.DatetimeIndex(pd.to_datetime(times, utc=True))
        return pd.DataFrame({"value": values}, index=idx)
    
    df = make(
        ["2026-10-01 00:10", "2026-10-01 00:59", "2026-10-01 02:30", "2026-10-01 02:40"],
        [1.0, 3.0, 10.0, np.nan],
    )

    print(hourly_stats(df))

   
