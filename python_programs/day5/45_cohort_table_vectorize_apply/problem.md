# Day 5 · Problem 9: Cohort table + vectorize an apply

Two functions in `main.py`.

## Part A: `cohort_retention(orders)`
`orders` has columns `user_id`, `order_ts` (tz-naive datetime). A user's **cohort** is the calendar month of their first order. `period` = months since cohort month (0 = the cohort month).

Return a DataFrame:
- index: cohort as strings `"YYYY-MM"`, sorted, index name `"cohort"`
- columns: integer periods `0..P` where `P` is the largest period observed anywhere, columns name `"period"`
- values: **fraction of the cohort's users** with at least one order in that period (a user ordering twice in one month counts once)
- A period that has not happened yet for a cohort (after the last month in the data) is **NaN**, not 0. A period that happened but had no active users is **0.0**.

Period 0 is always 1.0.

## Part B: `price_with_tax_fast(df)`
`price_with_tax_slow(df)` (given, row-wise `apply`) computes, per row:
- `base = price * qty`
- if `qty >= 10`, `base *= 0.9`
- tax rate is `0.05` if `category == "food"` else `0.18`
- result = `base * (1 + rate)` (no rounding)

Write `price_with_tax_fast(df)` returning a Series with the **same index and values** (within float tolerance) with **no row-wise apply**: use column arithmetic, `np.where` / `Series.map`. It must be at least 5x faster than the slow version on 30,000 rows.

## Watch out for
- Months between two dates: `(y2 - y1) * 12 + (m2 - m1)`. Not `.days / 30`.
- `nunique` per `(cohort, period)`, then divide by cohort size. `unstack(fill_value=0)` then NaN-mask the not-yet-happened cells.
- Don't mutate inputs.

## Interview angle
"Build a retention triangle from raw orders." and "This `apply(axis=1)` takes 20 minutes. Fix it."

## Run
```
pytest test_main.py -q
```
