# Day 3, Problem 6: Stable softmax and log-sum-exp

**Fact:** reductions take an `axis`; `keepdims=True` keeps shapes broadcastable.
**Gap from Problem 5:** row-wise ops need an `axis`.

## Task
Write two functions that stay finite for huge inputs:

- `logsumexp(x, axis=-1)` returns `log(sum(exp(x)))` along `axis` (that axis is removed).
- `softmax(x, axis=-1)` returns an array shaped like `x` that sums to 1 along `axis`.

## Examples
```python
softmax(np.array([1000., 1001., 1002.]))   # finite, sums to 1
logsumexp(np.array([1000., 1001., 1002.]))  # about 1002.41
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 06_stable_softmax
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/06_stable_softmax
git commit -m "day03-p06: stable_softmax"
```
