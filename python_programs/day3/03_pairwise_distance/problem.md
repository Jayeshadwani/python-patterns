# Day 3, Problem 3: Pairwise Euclidean distance matrix

**Fact:** inserting a length-1 axis lets every row meet every other row.
**Gap from Problem 2:** broadcasting gives pairwise operations.

## Task
Write `pairwise_distances(A, B)` where `A` has shape `(n, d)` and `B` has shape `(m, d)`.
Return an `(n, m)` matrix whose entry `[i, j]` is the Euclidean distance between `A[i]` and `B[j]`.

## Examples
```python
A = np.array([[0., 0.], [3., 4.]])
B = np.array([[0., 0.]])
pairwise_distances(A, B)   # [[0.], [5.]]
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 03_pairwise_distance
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/03_pairwise_distance
git commit -m "day03-p03: pairwise_distance"
```
