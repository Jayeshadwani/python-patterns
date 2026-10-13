# Day 4, Problem 8 (overall #35): Detecting row explosion with `validate`

**Fact:** if a key appears twice on either side, every left row with that key matches *every* right row with that key, so the merged table can have more rows than you started with.
**Gap from Problem 7:** the joins looked right, but nothing checked that keys were unique. A dirty lookup table silently multiplies rows and inflates every sum.
**Gap to Problem 9:** the table is now safe to build. The last step is changing its shape.

## Where this shows up
Joining facts to a lookup or dimension table (orders to customers, transactions to prices). A duplicate in the lookup table double counts revenue and nobody notices until a total looks wrong.

## Task
Write three functions in `main.py`.

1. `duplicate_keys(df, key)`: a **sorted Python list** of the values of column `key` that appear more than once. Missing values are ignored.
2. `row_growth(left, right, on, how="left")`: `len(merged) / len(left)` as a float for the merge on `on`. If `left` is empty, return `1.0`.
3. `checked_merge(left, right, on, how="left", validate="many_to_one")`: merge `left` and `right` on `on` using pandas `validate`. If pandas rejects the merge, raise `ValueError` with the message
   `merge is not <validate>: duplicate keys left=<list> right=<list>`
   where each list comes from `duplicate_keys` on that side. If the merge is valid, return the merged DataFrame exactly like `left.merge(right, on=on, how=how)`.

## Examples
```python
orders = pd.DataFrame({"order_id": [1, 2, 3, 4], "customer_id": [1, 2, 2, 3]})
dirty = pd.DataFrame({"customer_id": [1, 2, 3, 2], "name": ["Ana", "Ben", "Cy", "Ben (old)"]})
duplicate_keys(dirty, "customer_id")     # [2]
row_growth(orders, dirty, "customer_id") # 1.5   (4 rows became 6)
checked_merge(orders, dirty, "customer_id")
# ValueError: merge is not many_to_one: duplicate keys left=[2] right=[2]
```

## Rules
- Use pandas' own `validate=` to detect the problem. Do not hand-write the uniqueness check inside `checked_merge`.
- Do not modify the inputs.
- Say in 2-3 sentences what `many_to_one` and `one_to_one` each promise, before you code.

## Think first
1. `pd.errors.MergeError` is what pandas raises. Which built-in class does it inherit from, and why does the task still ask for your own message?
2. In a `left` join, how can a table end up with fewer rows than expected? (Answer: it cannot. Which case produces more?)

## Run
```
cd 35_merge_validation
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/35_merge_validation
git commit -m "day04-p08: merge_validation"
```
