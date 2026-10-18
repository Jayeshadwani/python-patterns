# Day 5 · Problem 3: Missing timestamps per site

**Topic:** `date_range`, `groupby`, set difference, finding gaps

## Task
Implement `missing_timestamps(df, freq="15min")` in `main.py`.

`df` has columns `site` (str), `ts` (tz-naive `datetime64`), `value`. Each site should report every `freq`. For **each site separately**, find the timestamps that are missing between **that site's own first and last `ts`**.

Return a DataFrame with columns exactly `["site", "ts"]`, one row per missing timestamp, sorted by `site` then `ts`, with a clean `RangeIndex` (0..n-1).

## Rules
- Duplicated timestamps for a site are **not** gaps and must not break anything.
- A site with a single row, or with no gaps, contributes **no** rows.
- Do not use one global date range for all sites. Site B's start/end differ from site A's.
- If nothing is missing anywhere, return an empty DataFrame that still has columns `["site", "ts"]`.

## Watch out for
- Is it better to build the full expected range and diff it, or to look at `diff()` between consecutive timestamps? (Either is fine, be ready to defend your choice.)
- Row order after `groupby` is not guaranteed to be sorted.

## Interview angle
"Your pipeline silently dropped rows for some sensors. How do you find which hours are missing, per sensor?"

## Run
```
pytest test_main.py -q
```
