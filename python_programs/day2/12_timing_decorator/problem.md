# Day 2, Problem 3 (overall #12): Timing decorator

**Fact:** a decorator is a function that takes a function and returns a new function. `@timer` above `def f` is shorthand for `f = timer(f)`.
**Gap from Problem 2:** the closure remembered a count. Here the closure remembers the original function and wraps extra behavior around it.

## Where this shows up
Whenever you add behavior around a function without editing its body: timing, logging, retries, auth checks, caching, input validation.

## Task
Write a decorator `timer(func)` so that the decorated function:
- is called with the same positional and keyword arguments, and returns the same result
- records how long the last call took, in seconds, on `wrapper.last_elapsed`
  (`None` before the first call)
- still records the time if the function raises, and the exception still propagates
- keeps the original function's `__name__` and `__doc__`

## Examples
```python
@timer
def slow_add(a, b=0):
    "Add two numbers slowly."
    time.sleep(0.05)
    return a + b

slow_add(1, b=2)            # 3
slow_add.last_elapsed       # about 0.05
slow_add.__name__           # 'slow_add'   (not 'wrapper')
slow_add.__doc__            # 'Add two numbers slowly.'
```

## Rules
- Use `functools.wraps` and `time.perf_counter`.
- The wrapper must accept any arguments (`*args, **kwargs`).
- Say in 2-3 sentences what runs when Python reads `@timer`, before you code.

## Run
```
cd 12_timing_decorator
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/12_timing_decorator
git commit -m "day02-p03: timing_decorator"
```