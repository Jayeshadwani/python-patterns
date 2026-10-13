# Day 3, Problem 8: Run-length encode with diff and flatnonzero

**Fact:** `np.diff` marks where neighbours differ; `np.flatnonzero` turns that into positions.
**Gap from Problem 7:** spotting boundaries with `diff`.

## Task
Write `run_length_encode(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]` for 1-D `x`.
Return `(values, lengths)`: each consecutive run's value and its length. Empty input
returns two empty arrays.

## Examples
```python
run_length_encode(np.array([1, 1, 2, 2, 2, 3]))
# (array([1, 2, 3]), array([2, 3, 1]))
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 08_run_length_encode
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/08_run_length_encode
git commit -m "day03-p08: run_length_encode"
```
