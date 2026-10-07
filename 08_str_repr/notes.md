# Pattern 08 — `__str__` vs `__repr__`

### `__str__`

Controls the **user-friendly** representation:

```python
print(person)
```

→ calls `__str__()`.

### `__repr__`

Controls the **developer/debug-friendly** representation:

```python
repr(person)
```

→ calls `__repr__()`.

### Core Difference

```text
__str__
→ readable for users

__repr__
→ useful for developers/debugging
```

**Key takeaway:**
`__str__` = human-friendly representation
`__repr__` = developer-friendly representation
