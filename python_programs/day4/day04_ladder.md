# Day 4: Pandas I (overall problems 28-36)

**Fact:** a DataFrame is a dict of equal-length columns sharing one index.

Folders: `28_loc_iloc_filters` ... `36_pivot_melt`. For each: read `problem.md`, say your approach in 2-3 sentences, fill `main.py`, run `python -m pytest -q` from inside the folder, then commit.

1. `28_loc_iloc_filters`: label vs position, boolean filters. So: filters pick rows, but what is each column stored as?
2. `29_dtypes_memory`: `astype`, `category`, downcasting. So: dtypes hide missing values.
3. `30_missing_group_median`: missing report and group-median `fillna`. So: we need group statistics.
4. `31_groupby_named_agg`: named aggregation, `size` vs `count`. So: a group stat often has to go back onto rows.
5. `32_groupby_transform`: z-score, share of total, group size per row. So: ranking inside groups.
6. `33_top_n_per_group`: top-N rows and n-th highest distinct value. So: tables must be joined.
7. `34_merge_joins`: inner, left, anti-joins. So: duplicate keys multiply rows.
8. `35_merge_validation`: `validate=` and row-growth detection. So: reshaping.
9. `36_pivot_melt`: wide to long and back, empty months. So: the time column is the trickiest one.

Recap: label -> dtype -> NaN -> group -> transform -> rank -> join -> fan-out -> reshape.

Commit pattern: `day04-pNN: short_name` (for example `day04-p01: loc_iloc_filters`).
