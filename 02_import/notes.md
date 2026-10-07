# Pattern 02 — `import` vs `from ... import ...`

### `import`

```python
import math_utils

math_utils.add(10, 5)
```

* Imports the **module**.
* Access its contents using `module_name.function()`.

### `from ... import ...`

```python
from math_utils import add

add(10, 5)
```

* Imports a **specific function/variable** from the module.
* Use it directly without the module name.

### Core Difference

```text
import module
→ module.function()

from module import function
→ function()
```

**Key takeaway:**
`import` → get the **module**
`from ... import ...` → get **specific things from the module**
