# Day 5 · Problem 8: Sessionization (diff + cumsum)

**Topic:** `groupby().diff()`, boolean flag, `cumsum` to label runs

## Task
Implement `sessionize(df, timeout="30min")` in `main.py`.

`df` has columns `user_id`, `ts` (tz-naive datetime), unsorted.

Return a **new** DataFrame sorted by `user_id` then `ts` with a clean `RangeIndex`, plus an integer column `session_no`:

- Numbering is **per user**, starting at **0**.
- A user's first event starts session 0.
- A new session starts when the gap to that user's previous event is **strictly greater** than `timeout`. A gap of exactly `timeout` stays in the same session.
- Sessions never span two users.

Fully vectorized: no Python loop over rows or users.

## Watch out for
- The first event of each user has `diff() == NaT`. What does `NaT > Timedelta` evaluate to? Is that what you want?
- `cumsum` on the flag must restart **per user**: `groupby(...).cumsum()` of the flag, not a global cumsum.
- Sort before diff.

## Interview angle
"Define a web session from raw clickstream in SQL/pandas." (Same idea in SQL: `LAG` + flag + running `SUM`.)

## Run
```
pytest test_main.py -q
```
