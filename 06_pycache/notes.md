# Pattern 06 — `__pycache__` and `.pyc`

When Python imports a module:

```text
.py
 ↓
compiled bytecode
 ↓
__pycache__/
 ↓
.pyc
```

* `__pycache__` stores Python's compiled bytecode.
* `.pyc` files are generated automatically.
* They are implementation/cache files, not source code.
* Usually add them to `.gitignore`.

**Key takeaway:**
`__pycache__` contains automatically generated `.pyc` bytecode files used by Python when loading modules.
