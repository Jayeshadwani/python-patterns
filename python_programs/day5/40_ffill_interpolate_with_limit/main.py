import pandas as pd
import numpy as np


def fill_short_gaps(s: pd.Series, max_gap: int) -> pd.Series:
    """See problem.md."""
    # 1. gap= consecutive runs of NaN values are gaps
    # 2. filling short gaps with interpolation
    # return the series

    s_copy = s.copy()

    # 1. Identify the gaps
    is_na = s.isna() # 2. True where a value is missing

    run_id = (is_na != is_na.shift()).cumsum() # 3. label each consecutive run

    gap_len = is_na.groupby(run_id).transform("sum") # 4. length of the NaN run each point belongs to

    filled = s.interpolate(method="time",limit_area="inside")

    filled[gap_len > max_gap] = np.nan

    return filled






    #missing_group_ids = np.unique(s_copy.loc[s_copy["is_missing"],["group_id"]])
    # 2. fill the gaps using interpolate method


    

if __name__ == "__main__":
    idx = pd.DatetimeIndex(["2026-10-01 00:00", "2026-10-01 01:00", "2026-10-01 04:00","2026-10-01 05:00","2026-10-01 06:00"])
    s = pd.Series([0.0, np.nan, 3.0, np.nan, np.nan], index=idx)

    res = fill_short_gaps(s,1)
    print(res)



