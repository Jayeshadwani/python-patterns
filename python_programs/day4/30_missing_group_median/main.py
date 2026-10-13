import pandas as pd


def missing_report(df: pd.DataFrame) -> pd.Series:
    """Fraction missing per column, only columns with missing values, descending."""
    df_missing = df.isna().mean()
    return df_missing[df_missing > 0].sort_values(ascending=False)


def fill_with_group_median(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Copy of df with NaN in value_col filled by the group median (see problem.md)."""
    df_copy = df.copy()
    df_copy[value_col] = df_copy.groupby(group_col,dropna=False)[value_col].transform(lambda x: fill_median(x, df_copy[value_col].median()))
    return df_copy

def fill_median(x: pd.Series, value_col_median: float) -> pd.Series:
    if x.name is None:
        return x.fillna(value_col_median)
    if pd.isna(x.median()):
        return x.fillna(value_col_median)
    else:
        return x.fillna(x.median()) 

def main():
    df = pd.DataFrame({"dept": ["A", "A", "A", "B", "B", "C", "C", None,None],
                       "salary": [10, None, 30, 40, None, None, None, None,40]})
    print(missing_report(df))
    print(fill_with_group_median(df, "dept", "salary"))


if __name__ == "__main__":
    main()
