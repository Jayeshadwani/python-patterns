# Day 4, Problem 2 (overall #29): dtypes, `astype` and `category`

**Fact:** every column has one dtype, and the dtype decides how much memory it takes and what operations are allowed.
**Gap from Problem 1:** filters pick rows. Now we ask what each column is stored as. Note that an integer column with a missing value silently becomes float, so dtypes also hide missing values.
**Gap to Problem 3:** once dtypes are right, we can deal with the missing values.

## Where this shows up
Big tables loaded from CSV arrive as `int64`, `float64` and plain text. Shrinking them is often the difference between a dataset that fits in RAM and one that does not, and a repeated-text column (city, status, country) is the biggest saving.

## Task
Write `shrink(df, cat_threshold=0.5)` in `main.py`. It returns a **new** DataFrame:

- integer columns are downcast to the smallest signed integer type that fits (`int8`, `int16`, `int32`, `int64`)
- float columns become `float32`
- text columns (`object` or string dtype) become `category` **only if** `nunique / len(df) < cat_threshold`; otherwise they stay as they are
- boolean columns and everything else are left alone
- values, column order and index are unchanged; missing values stay missing
- an empty DataFrame must not raise

## Examples
```python
df = pd.DataFrame({"age": [5, 70, 33], "city": ["Pune", "Pune", "Pune"]})
shrink(df).dtypes
# age       int8
# city  category
```

## Rules
- Do not modify the input DataFrame.
- No loops over rows (looping over columns is fine).
- Say in 2-3 sentences how you pick the rule for each dtype before you code.

## Think first
1. Why is the ratio `nunique / len` the right test for `category`, and what goes wrong for a column of unique ids?
2. Why does a column `[1, 2, NaN]` have dtype `float64`, and what does that do to an "integer downcast" rule?

## Run
```
cd 29_dtypes_memory
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/29_dtypes_memory
git commit -m "day04-p02: dtypes_memory"
```
