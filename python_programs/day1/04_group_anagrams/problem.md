# Day 1, Problem 4: Group anagrams

**Fact:** a dict finds a value by key without scanning.
**Gap from Problem 3:** the dict key was a number. Here the key must be derived from a word, and it must be hashable (a list cannot be a key).

## Task
Write `group_anagrams(words: List[str]) -> List[List[str]]` that groups words that
are anagrams of each other (same letters, same counts, any order).

Output order (so results are testable):
- groups appear in order of the first word of each group in the input
- words inside a group keep their input order

## Examples
```python
group_anagrams(["ab", "ba", "c"])
# [["ab", "ba"], ["c"]]

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

group_anagrams([])           # []
group_anagrams([""])         # [[""]]
```

## Rules
- Pure Python, no `Counter` as the grouping tool, no nested loops comparing every pair.
- Case-sensitive: "Ab" and "ab" are not anagrams.
- Say your approach in 2-3 sentences before coding.

## Run
```
cd 04_group_anagrams
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/04_group_anagrams
git commit -m "day01-p04: group_anagrams"
```