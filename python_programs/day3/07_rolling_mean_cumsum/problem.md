# Day 3, Problem 7: Rolling mean via cumsum

**Fact:** `cumsum` turns any window sum into a difference of two prefix sums.
**Gap from Problem 6:** sliding windows without loops.

## Task
Write `rolling_mean(x: np.ndarray, w: int) -> np.ndarray` for 1-D `x` and
`1 <= w <= len(x)`. Return an array of length `len(x) - w + 1` where element `i` is the
mean of `x[i:i+w]`.

## Examples
```python
rolling_mean(np.array([1., 2, 3, 4, 5]), 2)   # [1.5, 2.5, 3.5, 4.5]
rolling_mean(np.array([1., 2, 3, 4, 5]), 5)   # [3.]
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 07_rolling_mean_cumsum
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/07_rolling_mean_cumsum
git commit -m "day03-p07: rolling_mean_cumsum"
```
