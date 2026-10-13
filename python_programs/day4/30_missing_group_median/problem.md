# Day 4, Problem 3 (overall #30): Missing values and group-aware `fillna`

**Fact:** a missing value is `NaN` (or `None`/`NA`), and most pandas reductions skip it silently.
**Gap from Problem 2:** dtypes hid the missing values. Now we measure them and fill them, but filling every gap with one global number ignores that groups differ.
**Gap to Problem 4:** a "median of my group" is a group statistic, so we need `groupby`.

## Where this shows up
Before almost any model: report how much is missing per column, then impute. A salary gap in Engineering should be filled from Engineering, not from the whole company.

## Task
Write two functions in `main.py`.

1. `missing_report(df)`: a `Series` of the fraction of missing values per column, **only columns with at least one missing value**, sorted by fraction descending (ties keep column order). The index holds the column names.
2. `fill_with_group_median(df, group_col, value_col)`: returns a **copy** where missing values in `value_col` are replaced by the median of that row's group (computed ignoring missing values). Fallbacks:
   - if a group's values are all missing, use the overall median of `value_col`
   - if the row's group key is itself missing, use the overall median of `value_col`
   - if the whole column is missing, leave it as it is

## Examples
```python
df = pd.DataFrame({"dept":   ["A", "A", "A", "B", "B", "C", "C", None],
                   "salary": [10, None, 30, 40, None, None, None, None]})
fill_with_group_median(df, "dept", "salary")["salary"].tolist()
# [10.0, 20.0, 30.0, 40.0, 40.0, 30.0, 30.0, 30.0]
```

## Rules
- Do not modify the input DataFrame. Other columns and the index stay unchanged.
- No row loops.
- Say in 2-3 sentences how you get a per-row group median and what happens to rows with a missing group key, before you code.

## Think first
1. `df.groupby("dept")` drops rows whose key is missing. What does that do to a per-row result?
2. Which pandas groupby method returns one value **per original row** instead of one per group?

## Run
```
cd 30_missing_group_median
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/30_missing_group_median
git commit -m "day04-p03: missing_group_median"
```
