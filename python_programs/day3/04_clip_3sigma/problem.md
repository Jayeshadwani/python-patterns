# Day 3, Problem 4: Boolean mask: clip values beyond 3 sigma

**Fact:** a boolean mask selects elements; `np.where` chooses between two values.
**Gap from Problem 3:** distances need picking the smallest.

## Task
Write `clip_3sigma(x: np.ndarray) -> np.ndarray`. With `mu = x.mean()` and `sd = x.std()`,
values above `mu + 3*sd` become `mu + 3*sd`, values below `mu - 3*sd` become `mu - 3*sd`,
and everything else is unchanged. `x` must not be modified.

## Examples
```python
x = rng.normal(size=100); x[0] = 50
clip_3sigma(x)[0]          # about mu + 3*sd, far below 50
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 04_clip_3sigma
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/04_clip_3sigma
git commit -m "day03-p04: clip_3sigma"
```
