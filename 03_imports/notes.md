# Pattern 04 — Absolute vs Relative Imports

### Absolute import

```python
from utils.math_utils import add
```

* Starts from the package/module path.
* Common when importing from the project/package root.

### Relative import

```python
from .math_utils import add
```

* `.` means **current package**.
* Used when modules inside the same package import from each other.

### Core Difference

```text
Absolute:
from utils.math_utils import add

Relative:
from .math_utils import add
```

**Key takeaway:**
Absolute imports use the **full package path**.
Relative imports use the **current package as the starting point**.
