# Day 1, Problem 2: First non-repeating character

**Fact:** a dict finds a value by key without scanning.
**Gap from Problem 1:** counting tells you how many times, but not which came first.

## Task
Write `first_unique(s: str) -> Optional[str]` that returns the first character
that appears exactly once in `s`, or `None` if there is no such character.

## Examples
```python
first_unique("aabc")    # 'b'
first_unique("aabb")    # None
first_unique("")        # None
first_unique("xyx")     # 'y'
```

## Rules
- Pure Python, no `Counter`.
- Say your approach in 2-3 sentences before coding.
- Aim for O(n) time.

## Run
```
cd 02_first_unique
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/02_first_unique
git commit -m "day01-p02: first_unique"
```