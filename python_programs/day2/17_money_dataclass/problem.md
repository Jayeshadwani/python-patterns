# Day 2, Problem 8 (overall #17): Dataclass with ordering and hash (Money)

**Fact:** `@dataclass` writes the boring methods (`__init__`, `__repr__`, `__eq__`) from a list of fields, and options add more: `order=True` for sorting, `frozen=True` for immutability and hashing.
**Gap from Problem 7:** you wrote the iteration methods by hand. Dataclasses generate the common ones, but you must choose which ones to switch on, and equality and hashing have to agree.

## Where this shows up
Value objects: money, coordinates, versions, ids, config records, anything compared by value, sorted, or used as a dict key or set member.

## Task
Write a dataclass `Money` with two fields, in this order:
- `currency: str`
- `amount_cents: int` (cents as an integer, never a float)

It must:
- compare by value (`==`), and sort by currency first, then amount
- be hashable and immutable, so it works as a dict key or set member
- validate on creation: `amount_cents` must be an `int` (else `TypeError`), `currency` must be non-empty and `amount_cents` must not be negative (else `ValueError`)
- support `Money + Money` for the same currency, returning a new `Money`; different currencies raise `ValueError`; adding a non-`Money` raises `TypeError`
- print with `str()` as `"10.50 USD"` for `Money("USD", 1050)`

## Examples
```python
Money("USD", 1050)                          # Money(currency='USD', amount_cents=1050)
Money("USD", 100) + Money("USD", 250)       # Money(currency='USD', amount_cents=350)
str(Money("USD", 5))                        # '0.05 USD'
sorted([Money("USD", 300), Money("EUR", 900), Money("USD", 100)])
# [EUR 900, USD 100, USD 300]
{Money("USD", 1): "one cent"}               # works as a dict key
```

## Rules
- Use `@dataclass` with options. Do not write `__init__`, `__eq__`, `__hash__`, `__lt__` or `__repr__` yourself.
- You may write `__post_init__`, `__add__` and `__str__`.
- Say in 2-3 sentences which two options you turn on and what each one gives you, before you code.

## Run
```
cd 17_money_dataclass
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/17_money_dataclass
git commit -m "day02-p08: money_dataclass"
```