# Day 5 · Problem 2: resample hourly

**Topic:** `resample`, aggregation, bin edges, empty bins

## Task
Implement `hourly_stats(df)` in `main.py`.

`df` has a tz-aware (UTC) `DatetimeIndex` and a float column `value` (may contain NaN, unsorted index is possible).

Return a DataFrame indexed by **every hour** from the first event's hour to the last event's hour (no hour skipped), with columns exactly:

| column  | meaning                                  |
|---------|------------------------------------------|
| `mean`  | mean of non-null `value` in that hour    |
| `max`   | max of non-null `value` in that hour     |
| `count` | number of **non-null** `value` in that hour |

- Bins are **left-closed, left-labeled**: 00:00:00 to 00:59:59 is labeled 00:00; an event at exactly 01:00:00 belongs to hour 01.
- Hours with no data: `mean`/`max` are NaN, `count` is 0.

## Watch out for
- `count` vs `size`: which one ignores NaN?
- Does `resample` need a sorted index? What does it do to an empty bin?
- Alias: use `"1h"` (on pandas older than 2.2 use `"H"`).

## Interview angle
"`resample` vs `groupby(df.index.floor('h'))`: how do they differ on empty bins?"

## Run
```
pytest test_main.py -q
```
