**Day 1, Problem 1: Character frequency**

**Fact:** a dict finds a value by key without scanning.

**Task:** write `char_freq(s: str) -> dict` that returns how many times each character appears.

```python
char_freq("aab")      # {'a': 2, 'b': 1}
char_freq("")         # {}
char_freq("a b a")    # {'a': 2, ' ': 2, 'b': 1}
```

Pure Python, with no `Counter` for this one.

**First:** tell me your approach in 2-3 sentences, then paste your code. Ask for a hint if you're stuck.