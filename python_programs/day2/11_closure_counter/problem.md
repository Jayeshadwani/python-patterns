# Day 2, Problem 2 (overall #11): Closure counter

**Fact:** a function defined inside another function can keep using the outer function's variables, even after the outer function has returned.
**Gap from Problem 1:** the default argument was hidden state stored on the function, and it leaked by accident. Here you want hidden state on purpose: private to each counter, and shared by no one else.

## Where this shows up
Anywhere you need a function with its own private memory and no class: ID generators, call counters, rate limiters, memoizing wrappers, and (next problems) decorators.

## Task
Write `make_counter(start=0, step=1)` that returns a function. Each call to the
returned function adds `step` to the count and returns the new count.

## Examples
```python
c = make_counter()
c()                          # 1
c()                          # 2

d = make_counter(start=10, step=5)
d()                          # 15
d()                          # 20

a, b = make_counter(), make_counter()
a(); a()
b()                          # 1   (a and b do not share state)
```

## Rules
- The returned function must be a closure: use `nonlocal`.
- No `global`, no class, no default-argument trick.
- Say in 2-3 sentences where the count lives between calls before you code.

## Run
```
cd 11_closure_counter
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/11_closure_counter
git commit -m "day02-p02: closure_counter"
```