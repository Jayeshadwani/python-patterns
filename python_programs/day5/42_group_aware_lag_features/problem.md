# Day 5 · Problem 6: Group-aware lag features

**Topic:** `groupby().shift()`, sorting before shifting, leakage across groups

## Task
Implement `add_lag_features(df)` in `main.py`.

`df` has columns `site`, `ts` (tz-naive datetime), `value`. Rows are **unsorted** and sites are interleaved.

Return a **new** DataFrame, sorted by `site` then `ts`, with a clean `RangeIndex`, containing the original columns plus:

| column  | definition                                           |
|---------|------------------------------------------------------|
| `lag1`  | the previous `value` **of the same site** (1 row back by time) |
| `lag2`  | the `value` 2 rows back **of the same site**         |
| `delta` | `value - lag1`                                       |

The first row of each site must have NaN `lag1`/`delta`; the first two must have NaN `lag2`. A plain `df["value"].shift(1)` leaks the last value of the previous site into the first row of the next site. That is the bug this problem tests.

## Watch out for
- Sort **before** shifting. Shift on unsorted data is silently wrong.
- Don't mutate the input.

## Interview angle
"Your lag feature has suspiciously high importance and the model collapses in production. What do you check first?"

## Run
```
pytest test_main.py -q
```
