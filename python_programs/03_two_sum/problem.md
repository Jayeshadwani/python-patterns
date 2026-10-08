# Day 1, Problem 3: Two-sum with a hash map

**Fact:** a dict finds a value by key without scanning.
**Gap from Problem 2:** counting needed two passes. Can a pair question be answered in one pass?

## Task
Write `two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]` that
returns the indices `(i, j)` with `i < j` such that `nums[i] + nums[j] == target`,
or `None` if no such pair exists.

Assume there is at most one valid pair.

## Examples
```python
two_sum([2, 7, 11, 15], 9)   # (0, 1)
two_sum([3, 2, 4], 6)        # (1, 2)   # same element cannot be used twice
two_sum([3, 3], 6)           # (0, 1)
two_sum([1, 2, 3], 10)       # None
```

## Rules
- Pure Python, no nested loops (a nested loop is O(n^2), aim for O(n)).
- Return indices, not values.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 03_two_sum
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/03_two_sum
git commit -m "day01-p03: two_sum"
```