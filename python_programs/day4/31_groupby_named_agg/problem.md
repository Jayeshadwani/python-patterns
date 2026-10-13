# Day 4, Problem 4 (overall #31): `groupby` with named aggregation

**Fact:** `groupby` splits rows into groups by key, applies a reduction to each group, and combines the results into one row per group.
**Gap from Problem 3:** we needed "the median of my group" and used it as a helper. Here the group statistics are the answer itself.
**Gap to Problem 5:** a summary has one row per group. Often we need the group number back on every original row.

## Where this shows up
Every report or feature table: revenue per region, orders per customer, average basket per store. Named aggregation gives each output column an explicit name, so the table is readable and the meaning of "count" is not left to guesswork.

## Task
Write `sales_summary(df)` in `main.py`. The input has the columns `region`, `customer`, `amount`. Return one row per region with exactly these columns, in this order:

| column | meaning |
|---|---|
| `region` | the region (a normal column, not the index) |
| `orders` | number of **rows** in the region, including rows whose amount is missing |
| `customers` | number of distinct customers |
| `total` | sum of `amount` (missing values ignored; all missing gives `0.0`) |
| `avg` | mean of `amount` (missing values ignored; all missing gives `NaN`) |
| `largest` | max of `amount` (all missing gives `NaN`) |

Sort by `total` descending, ties by `region` ascending, and reset the index to `0..n-1`.

## Examples
```python
df = pd.DataFrame({"region":   ["N", "N", "S"],
                   "customer": ["c1", "c2", "c3"],
                   "amount":   [100, 50, None]})
sales_summary(df)
#   region  orders  customers  total    avg  largest
# 0      N       2          2  150.0   75.0    100.0
# 1      S       1          1    0.0    NaN      NaN
```

## Rules
- Use named aggregation (`.agg(name=("column", "func"))`). No loops over groups.
- Do not modify the input DataFrame.
- Say in 2-3 sentences how `orders` differs from `count` of the amount column, before you code.

## Think first
1. What is the difference between the aggregation functions `"size"` and `"count"`?
2. What happens to the group key when you finish: is it a column or the index?

## Run
```
cd 31_groupby_named_agg
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/31_groupby_named_agg
git commit -m "day04-p04: groupby_named_agg"
```
