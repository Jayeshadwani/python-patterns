# Day 3, Problem 2: Broadcasting: subtract column means

**Fact:** broadcasting stretches size-1 axes without copying data.
**Gap from Problem 1:** shapes can be stretched without copying.

## Task
Write `center_columns(X: np.ndarray) -> np.ndarray` that subtracts each column's mean
from `X` (shape `(n, d)`) and returns a new `(n, d)` array. `X` must not be modified.

## Examples
```python
center_columns(np.array([[1., 10.], [3., 20.]]))
# [[-1., -5.],
#  [ 1.,  5.]]
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 02_broadcasting_center
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/02_broadcasting_center
git commit -m "day03-p02: broadcasting_center"
```
