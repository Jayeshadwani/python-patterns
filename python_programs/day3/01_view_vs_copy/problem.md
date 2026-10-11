# Day 3, Problem 1: View vs copy

**Fact:** an array is one block of same-type numbers plus a shape.

## Task
Write three functions:

- `reshape_view(a)` returns `a` (6 elements) as shape `(2, 3)`, sharing memory with `a`.
- `reshape_copy(a)` returns the same shape, but independent of `a`.
- `reshape_shares_memory() -> bool` answers: does `a.reshape(2, 3)` share memory with a normal contiguous `a`?

## Examples
```python
a = np.arange(6)
v = reshape_view(a)
v[0, 0] = 99
a[0]                      # 99  (same block)
c = reshape_copy(a)
c[0, 0] = -1
a[0]                      # still 99
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 01_view_vs_copy
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/01_view_vs_copy
git commit -m "day03-p01: view_vs_copy"
```
