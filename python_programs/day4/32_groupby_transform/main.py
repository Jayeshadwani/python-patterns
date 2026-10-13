import pandas as pd


def zscore_within_group(df: pd.DataFrame, group_col: str, value_col: str) -> pd.Series:
    """(x - group mean) / group population std, aligned to df's index."""
    # return df.groupby(group_col)[value_col].transform(lambda x: (x - x.mean()) / x.std()) # x.std() computes standard deviation on sample data, denominator becomes n - 1
    def zscore(x):
        sd = x.std(ddof=0)
        if sd == 0:
            return pd.Series(0.0,index=x.index)
        else:
            return (x - x.mean()) / sd
    return df.groupby(group_col)[value_col].transform(zscore)


def share_of_group_total(df: pd.DataFrame, group_col: str, value_col: str) -> pd.Series:
    """x / group sum, aligned to df's index."""
    return df.groupby(group_col)[value_col].transform(lambda x: x / x.sum())


def group_size(df: pd.DataFrame, group_col: str) -> pd.Series:
    """Number of rows in each row's group, aligned to df's index."""
    # return df.groupby(group_col).size() # this outputs 1 row per group
    return df.groupby(group_col)[group_col].transform("size")
    

def main():
    df = pd.DataFrame({"g": ["a", "b", "a"], "v": [2.0, 10.0, 6.0]})
    print(share_of_group_total(df, "g", "v").tolist())
    print(group_size(df, "g").tolist())
    print(zscore_within_group(df, "g", "v").tolist())


if __name__ == "__main__":
    main()
