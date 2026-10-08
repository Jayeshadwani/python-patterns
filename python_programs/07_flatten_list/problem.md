# Day 1, Problem 7: Flatten a nested list

**Fact:** a function can call itself, and each call gets its own frame.
**Gap from Problem 6:** dicts had one level. Here a list can hold lists that hold lists, to any depth you cannot know in advance.

## Task
Write `flatten(nested: list) -> list` that returns a new flat list with all
non-list items in their original left-to-right order.

Only `list` objects are flattened. Anything else (ints, strings, tuples, None, dicts)
is a single item and is kept as is.

## Examples
```python
flatten([1, [2, [3]]])            # [1, 2, 3]
flatten([[1, 2], [3, [4, [5]]]])  # [1, 2, 3, 4, 5]
flatten(["ab", ["cd"]])           # ['ab', 'cd']   (a string is one item)
flatten([[], [[]]])               # []
```

## Rules
- Pure Python. Do not mutate the input.
- Use recursion.
- Say your approach in 2-3 sentences before coding. Name the base case and the recursive case.

## Run
```
cd 07_flatten_list
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/07_flatten_list
git commit -m "day01-p07: flatten_list"
```