import pandas as pd


def top_n_per_group(df: pd.DataFrame, group_col: str, value_col: str, n: int) -> pd.DataFrame:
    """Rows with the n largest values per group (see problem.md for ordering and ties)."""
    # return df.groupby(group_col)[value_col].rank(method="max") # this does not select n rows per group
    if n < 1:
        raise ValueError("n must be at least 1")

    result = (
        df.dropna(subset=[group_col, value_col])
          .groupby(group_col, sort=True, group_keys=False)
          .apply(lambda g: g.sort_values(value_col, ascending=False, kind="stable").head(n))
          .reset_index(drop=True)
    )

    return result
    # return df.groupby(group_col,group_keys=False).apply(lambda x: x.nlargest(n,value_col)).sort_values(by=[group_col, value_col], ascending=[True, False]).reset_index(drop=True)



def nth_highest_per_group(df: pd.DataFrame, group_col: str, value_col: str, n: int) -> pd.DataFrame:
    """Per group, the n-th highest distinct value; groups with fewer than n distinct values dropped."""

    if n < 1:
            raise ValueError("n must be at least 1")

    def select_nth(g):
        values = g[value_col].dropna().drop_duplicates().nlargest(n)

        if len(values) < n:
            return pd.DataFrame(columns=[group_col, value_col])

        return pd.DataFrame({
            group_col: [g.name],
            value_col: [values.iloc[-1]]
        })

    result = (
        df.dropna(subset=[group_col])
        .groupby(group_col, sort=True)
        .apply(select_nth)
        .reset_index(drop=True)
    )

    return result.sort_values(by=[group_col, value_col], ascending=[True, False]).reset_index(drop=True)


    ########## Approach 2 (less efficient, but simpler) ##########
    # df_copy['rank'] = df_copy.groupby(group_col)[value_col].rank(method='dense', ascending=False)
    # result = df_copy[df_copy['rank'] <= n].drop(columns=['rank']).sort_values(by=[group_col, value_col], ascending=[True, False]).reset_index(drop=True)

    # return result


def main():
    emp = pd.DataFrame({"dept": ["Eng", "Eng", "Eng", "Eng", "HR"],
                        "name": ["Ana", "Ben", "Cy", "Di", "Hal"],
                        "salary": [120, 100, 120, 90, 70]})
    print(top_n_per_group(emp, "dept", "salary", 2))
    print(nth_highest_per_group(emp, "dept", "salary", 2))


if __name__ == "__main__":
    main()
