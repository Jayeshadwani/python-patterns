# Day 2, Problem 6 (overall #15): batch(iterable, n)

**Fact:** a generator can pull items from another iterable a few at a time, bundle them, and yield the bundle, without loading the whole source.
**Gap from Problem 5:** `fibonacci` made values from nothing. `batch` consumes another iterable, which could be a generator or never end, so it must not call `list()` on it.

## Where this shows up
Anywhere work happens in chunks: bulk database inserts, API calls with a size limit, embedding or inference batches for a model, training mini-batches.

## Task
Write a generator `batch(iterable, n)` that yields lists of up to `n` items, in order.
The last list may be shorter. An empty input yields nothing.

`n` below 1 raises `ValueError` (when the generator is first iterated).

## Examples
```python
list(batch([1, 2, 3, 4, 5], 2))     # [[1, 2], [3, 4], [5]]
list(batch([1, 2, 3, 4], 2))        # [[1, 2], [3, 4]]       (no trailing empty list)
list(batch("abcde", 2))             # [['a', 'b'], ['c', 'd'], ['e']]
list(batch([], 3))                  # []

from itertools import count, islice
list(islice(batch(count(), 3), 2))  # [[0, 1, 2], [3, 4, 5]]   (works on infinite input)
```

## Rules
- It must be a generator (use `yield`). Do not call `list()` or `len()` on the input.
- It must read from the source only as needed: asking for the first batch of 3 must pull exactly 3 items.
- Each yielded batch is its own list (collecting all batches must still give correct results).
- Say in 2-3 sentences what you keep between yields and when you yield, before you code.

## Run
```
cd 15_batch_generator
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/15_batch_generator
git commit -m "day02-p06: batch_generator"
```