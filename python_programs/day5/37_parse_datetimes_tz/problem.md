# Day 5 · Problem 1: Parse datetimes, DatetimeIndex, tz

**Topic:** `pd.to_datetime`, `DatetimeIndex`, `tz_convert`, sorting, DST

## Scenario
Sensor events arrive as a raw DataFrame with columns:

| column  | meaning                                             |
|---------|-----------------------------------------------------|
| `ts`    | ISO-8601 string in **UTC**, e.g. `2026-10-31T12:00:00Z` |
| `site`  | site name                                           |
| `value` | float reading                                       |

Rows are **unsorted**, and some `ts` values are garbage (`"garbage"`, `None`).

## Task
Implement `load_events(df)` in `main.py`. It must return a **new** DataFrame where:

1. The index is a `DatetimeIndex` named `"ts"`, **tz-aware in `America/New_York`**
   (the instants must stay correct, so you are *converting* from UTC, not relabeling).
2. Rows whose `ts` cannot be parsed are **dropped**.
3. The index is **sorted ascending** and **unique** in the instants.
4. Columns are exactly `["site", "value"]` (the `ts` column is gone).
5. The input `df` is **not mutated**.

## Watch out for
- `01:30` happens **twice** on 2026-11-01 in New York (DST ends). Both rows must survive,
  as different instants (`-04:00` and `-05:00`).
- Localizing UTC wall-clock times as New York (`tz_localize`) is a different, wrong operation than converting.
- What does `pd.to_datetime` do on a bad string by default? How do you change that?

## Interview angle
"Why store timestamps in UTC and convert only for display?" Be ready to answer in one sentence.

## Run
```
pytest test_main.py -q
```
