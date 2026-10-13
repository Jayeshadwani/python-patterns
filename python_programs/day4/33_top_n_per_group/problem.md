# Day 4, Problem 6 (overall #33): Top-N per group (the "2nd highest salary" question)

**Fact:** ranking is a group operation too: "highest" only makes sense *inside* a group, and ties force you to decide what "2nd" means.
**Gap from Problem 5:** `transform` gave every row a group number. A rank is the same idea, one rank per row inside its group.
**Gap to Problem 7:** the answers are rows of one table. Real questions need data from two tables, so tables must be joined.

## Where this shows up
"Top 3 products per category", "latest order per customer", "second highest salary per department" are among the most common interview and analytics questions. The trap is always ties and missing values.

## Task
Write two functions in `main.py`. Both raise `ValueError` if `n < 1`.

1. `top_n_per_group(df, group_col, value_col, n)`: the rows holding the `n` largest `value_col` values in each group, **keeping all columns**. Rows with a missing value are ignored. Sort the result by group ascending, then value descending. Ties keep their original row order. Reset the index to `0..k-1`.
2. `nth_highest_per_group(df, group_col, value_col, n)`: a DataFrame with columns `[group_col, value_col]` holding, per group, the **n-th highest distinct value** (so `[120, 120, 100]` has 2nd highest `100`). Groups with fewer than `n` distinct values are left out. Sorted by group, index reset.

## Examples
```python
emp = pd.DataFrame({"dept": ["Eng", "Eng", "Eng", "Eng", "HR"],
                    "name": ["Ana", "Ben", "Cy", "Di", "Hal"],
                    "salary": [120, 100, 120, 90, 70]})
top_n_per_group(emp, "dept", "salary", 2)["name"].tolist()      # ['Ana', 'Cy', 'Hal']
nth_highest_per_group(emp, "dept", "salary", 2)                 # Eng -> 100 (HR has only one value)
```

## Rules
- No row loops and no Python-level loops over groups.
- Do not modify the input DataFrame.
- Say in 2-3 sentences how your two functions treat ties differently, before you code.

## Think first
1. `rank(method="first")`, `"min"` and `"dense"` all give different answers on ties. Which one matches "2nd highest distinct value"?
2. After sorting, which groupby method keeps only the first `n` rows of each group?

## Run
```
cd 33_top_n_per_group
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/33_top_n_per_group
git commit -m "day04-p06: top_n_per_group"
```
