# Pattern 05 — `__all__`

```python
__all__ = ["add"]
```

Controls which names are exposed when using:

```python
from utils import *
```

Example:

```python
__all__ = ["add"]
```

→ `add` is imported
→ `subtract` is not imported

**Key takeaway:**
`__all__` controls what gets exported by `from module import *`.
