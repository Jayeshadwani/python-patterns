# Day 4, Problem 9 (overall #36): `melt` and `pivot`, wide to long and back

**Fact:** the same data can be stored *wide* (one column per category) or *long* (one row per observation). `melt` goes wide to long, `pivot` goes long to wide.
**Gap from Problem 8:** the table is now correct. The last step is giving it the shape the next tool wants: plots and models want long, human reports want wide.
**Gap to Day 5:** the trickiest column to reshape is time. Months with no data do not appear in a pivot at all, so holes have to be found and filled on purpose.

## Where this shows up
Survey and score tables arrive wide and must be melted before grouping or plotting. Reports and model features are built by pivoting long event data into one column per category, with `0` or `NaN` where nothing happened.

## Task
Write three functions in `main.py`.

1. `wide_to_long(df)`: `df` has a `student` column plus one column per subject. Return a long table with columns `student, subject, score`, **dropping rows whose score is missing**, sorted by `student` then `subject`, index reset.
2. `long_to_wide(df)`: `df` has `student, subject, score`. Return one row per student and one column per subject. Duplicate (student, subject) pairs are **averaged**. Missing combinations are `NaN`. Columns: `student` first, then subjects in alphabetical order. Rows sorted by `student`, index reset, and `columns.name` must be `None`.
3. `monthly_totals(df)`: `df` has `date` (text like `"2024-01-05"`), `region`, `amount`. Return one row per **calendar month between the first and the last month in the data, inclusive**, even months with no rows. Columns: `month` (text like `"2024-01"`), then one column per region in alphabetical order holding the total `amount`, with `0` where there is nothing. Sorted by month, index reset, `columns.name` is `None`.

## Examples
```python
wide = pd.DataFrame({"student": ["Ana", "Ben"], "math": [90, 70], "chem": [None, 60]})
wide_to_long(wide)
#   student subject  score
# 0     Ana    math   90.0
# 1     Ben    chem   60.0
# 2     Ben    math   70.0
```

## Rules
- Use `melt` and `pivot_table` (or `pivot`), not loops.
- Do not modify the input DataFrames.
- Say in 2-3 sentences which function fails on duplicate pairs (`pivot` or `pivot_table`) and how you find the empty months, before you code.

## Think first
1. `df.pivot(...)` raises an error when a (row, column) pair repeats. What does `pivot_table` do instead?
2. If February has no rows at all, will a pivot on `month` show a February row? How can you force it?

## Run
```
cd 36_pivot_melt
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/36_pivot_melt
git commit -m "day04-p09: pivot_melt"
```
