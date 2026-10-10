# Day 2, Problem 9 (overall #18): Context managers (Timer and swallow)

**Fact:** `with obj:` calls `obj.__enter__()` on the way in and `obj.__exit__(exc_type, exc, tb)` on the way out, and `__exit__` runs even when the block raises.
**Gap from Problem 8:** dataclasses generated methods for you. Here Python calls two methods at fixed moments, and what `__exit__` returns decides whether an exception survives.

## Where this shows up
Any "set something up, do work, always put it back" situation: opening and closing files, taking and releasing locks, committing or rolling back transactions, temporarily changing a setting, timing a block.

## Task
Write two context managers in `main.py`.

**1. `Timer` (a class with `__enter__` / `__exit__`)**
- `with Timer() as t:` gives you the Timer itself as `t`.
- `t.elapsed` is `None` before and during the block, and the block's duration in seconds (a float) after it.
- `elapsed` is set even if the block raises, and the exception still propagates.
- Reusing the same Timer in a second `with` overwrites `elapsed`.

**2. `swallow(*exc_types)` (a generator function using `@contextlib.contextmanager`)**
- Exceptions that are instances of `exc_types` (subclasses included) are suppressed, and execution continues after the `with` block.
- Any other exception propagates unchanged.
- With no arguments it suppresses nothing.
- The rest of the block after the line that raised does not run.

## Examples
```python
with Timer() as t:
    time.sleep(0.05)
t.elapsed                      # ~0.05

with swallow(KeyError):
    {}["missing"]
print("still running")         # reached

with swallow(KeyError):
    int("x")                   # ValueError, not swallowed -> propagates
```

## Rules
- `Timer` must be a class; `swallow` must be a generator function decorated with `@contextmanager`.
- Use `time.perf_counter()` for timing.
- Say in 2-3 sentences what `__exit__` must return for an exception to propagate, and what `swallow` does at `yield` when the block raises, before you code.

## Run
```
cd 18_context_manager
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/18_context_manager
git commit -m "day02-p09: context_manager"
```