# Day 3, Problem 5: One-hot encode with fancy indexing

**Fact:** an integer array can index several positions at once (fancy indexing).
**Gap from Problem 4:** masks pick, but `where` chooses.

## Task
Write `one_hot(labels: np.ndarray, num_classes: int) -> np.ndarray`. `labels` is an int
array of shape `(n,)`. Return a float array of shape `(n, num_classes)` with a single `1.0`
per row, at the column given by that row's label.

## Examples
```python
one_hot(np.array([0, 2, 1]), 3)
# [[1., 0., 0.],
#  [0., 0., 1.],
#  [0., 1., 0.]]
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 05_one_hot
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/05_one_hot
git commit -m "day03-p05: one_hot"
```
