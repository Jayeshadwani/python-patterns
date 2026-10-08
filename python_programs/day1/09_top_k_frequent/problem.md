# Day 1, Problem 9: Top-k frequent words

**Fact:** a heap keeps the smallest (or largest) item easy to reach without sorting everything.
**Gap from Problem 8:** a stack gives the most recent item back. Here you need the *most frequent* ones. Sorting every word orders all m unique words even when you only want k of them.

## Task
Write `top_k_frequent(words: List[str], k: int) -> List[str]` that returns the
`k` most frequent words.

Order of the result:
- higher frequency first
- if two words have the same frequency, the alphabetically smaller word first

If `k` is larger than the number of unique words, return all unique words.

## Examples
```python
top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
# ['i', 'love']

top_k_frequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
# ['the', 'is', 'sunny', 'day']

top_k_frequent(["b", "a", "c"], 2)    # ['a', 'b']   (all tie, alphabetical)
top_k_frequent([], 3)                 # []
```

## Rules
- Use `collections.Counter` to count and `heapq` to pick the top k.
- Say your approach in 2-3 sentences before coding. State the time complexity.
- After it passes, compare against a version that sorts all unique words. When is each faster?

## Run
```
cd 09_top_k_frequent
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/09_top_k_frequent
git commit -m "day01-p09: top_k_frequent"
```