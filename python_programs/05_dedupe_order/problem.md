# Day 1, Problem 5: Dedupe preserving order

**Fact:** a dict finds a value by key without scanning.
**Gap from Problem 4:** you used a dict to group. A `set` also removes duplicates, but what does it forget?

## Task
Write `dedupe(items: List[Any]) -> List[Any]` that returns a new list with
duplicates removed, keeping the first occurrence of each item and the original order.

All items are hashable.

## Examples
```python
dedupe([3, 1, 3, 2])          # [3, 1, 2]
dedupe(["b", "a", "b"])       # ['b', 'a']
dedupe([1, 1, 1])             # [1]
dedupe([])                    # []
```

## Rules
- Pure Python. Do not mutate the input list.
- Aim for O(n) time. `if x not in result_list` is O(n) per check, so it is O(n^2) overall.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 05_dedupe_order
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/05_dedupe_order
git commit -m "day01-p05: dedupe_order"
```