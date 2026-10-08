# Day 1, Problem 6: Merge two dicts, summing values

**Fact:** a dict finds a value by key without scanning.
**Gap from Problem 5:** the dict value there was a throwaway ("Seen"). Here the value matters and must be combined.

## Task
Write `merge_dicts(a: Dict[str, float], b: Dict[str, float]) -> Dict[str, float]`
that returns a new dict containing every key from `a` and `b`.
If a key is in both, its value is the sum of the two values.

## Examples
```python
merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})   # {'a': 1, 'b': 5, 'c': 4}
merge_dicts({}, {"x": 1})                         # {'x': 1}
merge_dicts({"x": 1}, {})                         # {'x': 1}
merge_dicts({}, {})                               # {}
```

## Rules
- Pure Python. Do not mutate `a` or `b`.
- A key whose sum is 0 stays in the result.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 06_merge_dicts
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/06_merge_dicts
git commit -m "day01-p06: merge_dicts"
```