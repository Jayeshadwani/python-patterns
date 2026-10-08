# Day 1, Problem 8: Valid parentheses

**Fact:** a stack gives back the most recently added item first (last in, first out). A Python list does this with `append` and `pop`.
**Gap from Problem 7:** recursion remembered "where am I" on a hidden call stack. Here you must remember which brackets are still open, and the most recent one must close first.

## Task
Write `is_valid(s: str) -> bool` that returns `True` if every bracket in `s` is
closed by the same type of bracket, in the correct order.

`s` contains only these characters: `()[]{}`

## Examples
```python
is_valid("()")        # True
is_valid("()[]{}")    # True
is_valid("{[]}")      # True
is_valid("(]")        # False   (wrong type)
is_valid("([)]")      # False   (wrong order)
is_valid("(")         # False   (never closed)
is_valid(")")         # False   (closes nothing)
is_valid("")          # True
```

## Rules
- Pure Python. Use a list as a stack (`append` / `pop`).
- O(n) time, one pass.
- Say your approach in 2-3 sentences before coding. Name what you push, and when you pop.

## Run
```
cd 08_valid_parentheses
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/08_valid_parentheses
git commit -m "day01-p08: valid_parentheses"
```