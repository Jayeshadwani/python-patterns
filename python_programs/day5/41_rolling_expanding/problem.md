# Day 5 · Problem 5: rolling and expanding

**Topic:** row-based vs time-based windows, `min_periods`, `expanding`, leakage

## Task
Implement `add_window_features(df)` in `main.py`.

`df` has a sorted `DatetimeIndex` (irregular spacing) and a float column `value`. Return a **copy** with these extra columns (keep `value`):

| column       | definition                                                                 |
|--------------|----------------------------------------------------------------------------|
| `roll3`      | mean of the **last 3 rows including current**; NaN until 3 rows exist      |
| `roll7d`     | mean over the **time window** `(t - 7 days, t]` including current row      |
| `exp_mean`   | expanding mean of all rows up to and including current                     |
| `roll3_prev` | mean of the **3 rows before** the current one (current excluded); NaN until 3 prior rows exist |

## Watch out for
- `rolling(3)` counts **rows**; `rolling("7D")` is **time based**. With irregular timestamps they give different answers.
- A time window `"7D"` is closed on the right by default: the row exactly 7 days earlier is **excluded**.
- `roll3_prev` is the leakage-safe feature for predicting the current value. How do you build it without a second rolling call that sees the current row?
- Don't mutate the input.

## Interview angle
"Why is a centered rolling mean a leak in a forecasting feature?"

## Run
```
pytest test_main.py -q
```
