# Pattern 04 — `python file.py` vs `python -m`

### `python file.py`

```bash
python utils/calculator.py
```

→ Runs the file as a standalone script.

### `python -m`

```bash
python -m utils.calculator
```

→ Runs the file as a module within its package.

### Core Difference

```text
python file.py
→ Run as a file

python -m package.module
→ Run as a module
```

**Key takeaway:**
`-m` tells Python to understand the **package/module structure**, which is important for relative imports.
