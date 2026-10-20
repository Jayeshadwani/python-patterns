# Day 5 · Problem 7: Time-based train/test split

**Topic:** chronological split, purge gap, tz-aware vs tz-naive comparison

## Task
Implement `time_split(df, cutoff, gap="0D")` in `main.py`.

`df` has a tz-aware (UTC) `DatetimeIndex` (possibly unsorted). `cutoff` is either a string like `"2026-01-07"` or a `pd.Timestamp`. A tz-naive cutoff means **UTC**.

Return `(train, test)`:

- `test`  = rows with `index >= cutoff`
- `train` = rows with `index < cutoff - gap`   (`gap` is anything `pd.Timedelta` accepts, e.g. `"2D"`)
- Rows inside the gap `[cutoff - gap, cutoff)` belong to **neither** set (this purge avoids leakage from features computed on overlapping windows).
- Both outputs sorted ascending by index. Never shuffle.
- Raise `ValueError` if **either** output would be empty.

## Watch out for
- Comparing a tz-aware index with a tz-naive timestamp raises `TypeError`. Make the cutoff tz-aware first.
- Why is `train_test_split(shuffle=True)` wrong for time series?

## Interview angle
"Your offline AUC is 0.95 and production AUC is 0.70. The split was random. Why?"

## Run
```
pytest test_main.py -q
```
