# Day 3, Problem 9: Cosine-similarity top-k with matmul and argpartition

**Fact:** a matrix product computes every dot product at once; `argpartition` finds the top k without a full sort.
**Gap from Problem 8:** similarity is a matmul.

## Task
Write `cosine_topk(Q, D, k)` where `Q` is `(nq, d)` queries, `D` is `(nd, d)` documents
and `1 <= k <= nd`. Return `(idx, scores)`, both shaped `(nq, k)`: the indices of the `k`
most cosine-similar documents per query and their similarities, sorted descending.

## Examples
```python
Q = np.array([[1., 0.]])
D = np.array([[1., 0.], [0., 1.], [1., 1.]])
cosine_topk(Q, D, 2)
# (array([[0, 2]]), array([[1.  , 0.707...]]))
```

## Rules
- NumPy only, no Python loops over elements.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 09_cosine_topk
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/09_cosine_topk
git commit -m "day03-p09: cosine_topk"
```
