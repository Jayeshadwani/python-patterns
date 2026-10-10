# Day 2, Problem 7 (overall #16): Iterator class (sliding window)

**Fact:** a `for` loop calls `iter(obj)` to get an iterator, then calls `next()` on it until it raises `StopIteration`.
**Gap from Problem 6:** a generator wrote that machinery for you when you used `yield`. Here you write it by hand, so you see what a generator was doing.

## Where this shows up
Objects you can loop over more than once: datasets, file readers, paged API results, rolling windows of sensor or time-series values.

## Task
Write two classes:

1. `WindowIterator(data, size)`: the iterator. `__next__` returns the next window as a tuple of `size` consecutive items and raises `StopIteration` when there are no more. `__iter__` returns itself.
2. `SlidingWindow(data, size)`: the iterable. `__iter__` returns a **new** `WindowIterator` each time. `size < 1` raises `ValueError` when the object is created.

If `size` is larger than the data, there are no windows.

## Examples
```python
list(SlidingWindow([1, 2, 3, 4], 2))   # [(1, 2), (2, 3), (3, 4)]
list(SlidingWindow("abcd", 3))         # [('a', 'b', 'c'), ('b', 'c', 'd')]
list(SlidingWindow([1, 2], 5))         # []

w = SlidingWindow([1, 2, 3], 2)
list(w)                                # [(1, 2), (2, 3)]
list(w)                                # [(1, 2), (2, 3)]   (can be looped again)
```

## Rules
- No `yield` anywhere. Write `__iter__` and `__next__` yourself.
- Looping twice over the same `SlidingWindow` must give the same result.
- Two iterators from the same `SlidingWindow` must not affect each other.
- Say in 2-3 sentences where the position is stored, and why `SlidingWindow` is not its own iterator, before you code.

## Run
```
cd 16_window_iterator
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/16_window_iterator
git commit -m "day02-p07: window_iterator"
```