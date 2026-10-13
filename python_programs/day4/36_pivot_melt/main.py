import pandas as pd


def wide_to_long(df: pd.DataFrame) -> pd.DataFrame:
    """student + one column per subject  ->  student, subject, score (NaN scores dropped)."""
    # value_vars is not required attribute
    return pd.melt(df, id_vars="student", var_name="subject", value_name="score").dropna(subset=["score"]).sort_values(["student", "subject"]).reset_index(drop=True)


def long_to_wide(df: pd.DataFrame) -> pd.DataFrame:
    """student, subject, score  ->  one row per student, one column per subject (mean on duplicates)."""
    # pivot() raises an error when a (row, column) pair repeats because it cannot choose which value to use.
    # pivot_table() aggregates the repeated values using aggfunc, such as "mean", "sum", or "count".
    out = pd.pivot_table(
        df,
        index="student",
        columns="subject",
        values="score",
        aggfunc="mean"
    ).reset_index()

    out.columns.name = None
    return out[["student"] + sorted(c for c in out.columns if c != "student")]


def monthly_totals(df: pd.DataFrame) -> pd.DataFrame:
    """month x region totals, including empty months between first and last month."""
    # 1. create month column in df_copy
    df_copy = df.copy()
    df_copy["date"] = pd.to_datetime(df_copy["date"])
    df_copy["month"] = df_copy["date"].dt.to_period("M")


    # 2. apply pivot_table to df, index as region, and columns as month
    all_months = pd.period_range(
        df_copy["month"].min(),
        df_copy["month"].max(),
        freq="M"
    )

    out = pd.pivot_table(
        df_copy,
        index="month",
        columns="region",
        values="amount",
        aggfunc="sum",
        fill_value=0
    ).reindex(all_months, fill_value=0)

    # 3. sorting 
    out.index.name = "month"
    out = out.reset_index()
    out["month"] = out["month"].astype(str)
    out.columns.name = None

    return out[["month"] + sorted(c for c in out.columns if c != "month")]
    


def main():
    wide = pd.DataFrame({"student": ["Ana", "Ben"], "math": [90, 70], "chem": [None, 60]})
    print(wide_to_long(wide))
    # long = wide_to_long(wide)
    # print(long_to_wide(long))
    sales = pd.DataFrame({"date": ["2024-01-05", "2024-03-02"],
                          "region": ["N", "S"], "amount": [100, 70]})
    print(monthly_totals(sales))


if __name__ == "__main__":
    main()
