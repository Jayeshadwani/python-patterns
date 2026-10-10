# Day 2, Problem 5 (overall #14): Generators, a lazy Fibonacci

**Fact:** `yield` pauses a function and keeps its local variables. The next `next()` resumes right after the `yield`.
**Gap from Problem 4:** a closure remembered values in variables. A generator remembers values *and where it is in the code*.

## Where this shows up
Sequences that are huge or never end, and streams you want to process one item at a time without building a list: reading big files, paging through an API, feeding batches to a model.

## Task
Write two generator functions:

1. `fibonacci()` yields the Fibonacci numbers forever: 0, 1, 1, 2, 3, 5, 8, ...
2. `fib_below(limit)` yields the Fibonacci numbers that are strictly less than `limit`, then stops.

## Examples
```python
from itertools import islice

list(islice(fibonacci(), 10))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
list(fib_below(10))             # [0, 1, 1, 2, 3, 5, 8]
list(fib_below(0))              # []
```

## Rules
- Both must be real generators (use `yield`), not functions that return a list.
- Do not store the whole sequence anywhere. Keep only what the next value needs.
- No recursion.
- Say in 2-3 sentences what must be remembered between two `yield`s, before you code.

## Run
```
cd 14_fibonacci_generator
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/14_fibonacci_generator
git commit -m "day02-p05: fibonacci_generator"
```