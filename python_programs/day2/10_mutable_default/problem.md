# Day 2, Problem 1 (overall #10): Mutable default argument bug

**Fact:** a default value is created once, when `def` runs, not each time the function is called.
**Gap from Day 1:** you used lists and dicts as accumulators. A function that builds up a list, dict or set across calls is exactly where this bug hides.

## Where this shows up
Any function that takes an optional list, dict or set and adds to it: collecting results, caches, config merging, logging helpers.

## Task
`main.py` contains a buggy `add_item`. Fix it so that:
- called without `items`, each call starts with a fresh empty list
- called with a list, it appends to **that** list and returns the same list object
- an explicitly passed empty list is still used (not replaced)

## Examples
```python
add_item(1)            # [1]
add_item(2)            # [2]        (buggy version returns [1, 2])

lst = []
add_item(1, lst)
add_item(2, lst)
lst                    # [1, 2]
```

## Rules
- Keep the signature `add_item(item, items=...)`.
- Say in 2-3 sentences *why* the buggy version misbehaves before you fix it.

## Run
```
cd 10_mutable_default
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/10_mutable_default
git commit -m "day02-p01: mutable_default"
```
