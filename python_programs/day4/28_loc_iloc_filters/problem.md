# Day 4, Problem 1 (overall #28): loc vs iloc and boolean filters

**Fact:** a DataFrame is a dict of equal-length columns sharing one index. Every row has a *label* (the index value) and a *position* (0, 1, 2, ...), and they are only the same by accident.
**Gap to Problem 2:** filters pick rows. The next question is what type each column holds.

## Where this shows up
Any time a DataFrame has been filtered, sorted, or concatenated, its index stops being 0..n-1. Code that assumed label == position then silently returns the wrong rows.

## Task
Write four functions in `main.py`. The test DataFrame deliberately has the index `[30, 10, 20, 40]`.

1. `first_n(df, n)`: the first `n` rows **by position** (all rows if `n` is larger than the frame).
2. `by_labels(df, labels)`: the rows whose index **label** is in `labels`, in the order given. A missing label must raise `KeyError`.
3. `filter_city_age(df, city, min_age)`: rows where `city` equals `city` and `age >= min_age`, returning only the columns `name` and `age`. The original index is kept. Use one `.loc[mask, columns]` call.
4. `last_row_name(df)`: the `name` of the last row **by position**.

## Examples
```python
df = pd.DataFrame({"name": ["Ana", "Ben", "Cleo", "Dev"],
                   "age": [34, 19, 41, 27],
                   "city": ["Pune", "Delhi", "Pune", "Pune"]},
                  index=[30, 10, 20, 40])
first_n(df, 2).index.tolist()                  # [30, 10]
by_labels(df, [40, 10]).index.tolist()         # [40, 10]
filter_city_age(df, "Pune", 30).index.tolist() # [30, 20]
last_row_name(df)                              # 'Dev'
```

## Rules
- Do not modify the input DataFrame.
- No loops.
- Say in 2-3 sentences which of `loc` / `iloc` each function needs and why, before you code.

## Think first
1. What does `df.loc[0]` do on this frame? What does `df.iloc[0]` do?
2. Why is `df["name"][-1]` not a safe way to get the last value?

## Run
```
cd 28_loc_iloc_filters
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/28_loc_iloc_filters
git commit -m "day04-p01: loc_iloc_filters"
```
