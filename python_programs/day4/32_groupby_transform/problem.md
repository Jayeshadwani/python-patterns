# Day 4, Problem 5 (overall #32): `groupby.transform`, group statistics back on rows

**Fact:** `agg` returns one value per group. `transform` returns one value per original row, in the original order, by repeating each group's result on the rows of that group.
**Gap from Problem 4:** a summary table loses the rows. Here we keep every row and attach a group-aware number to it.
**Gap to Problem 6:** a group number per row lets us compare a row to its group, which leads to ranking inside groups.

## Where this shows up
Feature engineering: "salary relative to my department", "share of my store's sales", "how many rows are in my group". Normalizing inside a group removes the group effect so that a model sees how unusual a row is for its group.

## Task
Write three functions in `main.py`. Each returns a `Series` with **the same index and row order as the input**.

1. `zscore_within_group(df, group_col, value_col)`: `(x - group mean) / group std`, using the **population** standard deviation (`ddof=0`). If a group's std is `0` (for example a one-row group), the result is `0.0`. Missing values stay missing and are ignored in the group mean and std.
2. `share_of_group_total(df, group_col, value_col)`: `x / group sum`. Assume values are positive.
3. `group_size(df, group_col)`: the number of rows in the row's group.

## Examples
```python
df = pd.DataFrame({"g": ["a", "b", "a"], "v": [2.0, 10.0, 6.0]})
share_of_group_total(df, "g", "v").tolist()   # [0.25, 1.0, 0.75]
group_size(df, "g").tolist()                  # [2, 1, 2]
```

## Rules
- Use `groupby(...).transform(...)`. Do not build a summary table and merge it back.
- Do not modify the input DataFrame.
- Say in 2-3 sentences why `transform` is a better fit than `agg` followed by `merge`, before you code.

## Think first
1. If the index is shuffled like `[5, 3, 9, ...]`, what would go wrong if you used `agg` and then assigned the result by position?
2. `Series.std()` uses `ddof=1` by default. Which value does this problem need?

## Run
```
cd 32_groupby_transform
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/32_groupby_transform
git commit -m "day04-p05: groupby_transform"
```
