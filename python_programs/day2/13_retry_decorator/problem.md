# Day 2, Problem 4 (overall #13): retry(n) decorator with arguments

**Fact:** a decorator with settings is a function that returns a decorator. `@retry(3)` first calls `retry(3)`, and the result is then applied to the function.
**Gap from Problem 3:** `timer` took only the function. Here the decorator also needs its own settings (how many attempts), so there is one more layer.

## Where this shows up
Calling things that fail for temporary reasons: network requests, database connections, file locks, flaky model or API endpoints.

## Task
Write `retry(max_attempts, exceptions=(Exception,))` so that a decorated function:
- is called again when it raises one of `exceptions`, up to `max_attempts` calls in total
- returns the result of the first successful call
- if every attempt fails, raises the exception from the last attempt
- does not retry exceptions that are not in `exceptions` (they propagate at once)
- keeps its `__name__` and `__doc__`
- each invocation starts counting from zero

`retry(0)` and `retry(-1)` raise `ValueError` when the decorator is created.

## Examples
```python
@retry(3)
def fetch():
    ...            # raises twice, then succeeds -> returns the value, 3 calls made

@retry(2, exceptions=(KeyError,))
def lookup():
    raise ValueError("no retry")   # ValueError propagates after 1 call
```

## Rules
- No sleeping or backoff yet (that comes on Day 11).
- Say in 2-3 sentences what the three nested functions are and when each one runs.

## Run
```
cd 13_retry_decorator
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/13_retry_decorator
git commit -m "day02-p04: retry_decorator"
```