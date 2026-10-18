# Day 5 · Problem 4: ffill / interpolate with limit

**Topic:** gap-aware filling, `interpolate(method="time")`, run lengths of NaN

## Task
Implement `fill_short_gaps(s, max_gap)` in `main.py`.

`s` is a float `Series` with a `DatetimeIndex` (may be irregular). A **gap** is a maximal run of consecutive NaN values.

- Gaps of length `<= max_gap` that are **between two known values** are filled by **time-weighted linear interpolation** (`method="time"`, i.e. weighted by the actual timestamps, not by row position).
- Gaps of length `> max_gap` are left **entirely NaN**.
- **Leading and trailing** NaNs are never filled (no extrapolation, no ffill/bfill).
- `max_gap=0` leaves the series unchanged.
- Return a **new** Series with the same index and name. Do not mutate the input.

## Watch out for
- The classic trap: `interpolate(limit=2)` fills the **first 2** NaNs of a longer gap and leaves the rest. That is NOT what this problem wants. A long gap must stay fully NaN.
- `limit_area="inside"` helps with the leading/trailing rule.
- To get gap lengths: label runs with `(isna != isna.shift()).cumsum()`, then size each run.

## Interview angle
"Fill short sensor dropouts but never invent data across a long outage. How?"

## Run
```
pytest test_main.py -q
```
