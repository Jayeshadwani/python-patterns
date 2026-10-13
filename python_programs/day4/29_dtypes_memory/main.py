import pandas as pd


def shrink(df: pd.DataFrame, cat_threshold: float = 0.5) -> pd.DataFrame:
    """Return a new DataFrame with smaller dtypes (see problem.md)."""
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include=[float]).columns:
        df_copy[col] = pd.to_numeric(df_copy[col], downcast="float")
    for col in df_copy.select_dtypes(include=[int]).columns:
        df_copy[col] = pd.to_numeric(df_copy[col], downcast="integer")
    for col in df_copy.select_dtypes(include=[object]).columns:
        if (len(df) > 0) and (df_copy[col].nunique() / len(df) < cat_threshold):
            df_copy[col] = df_copy[col].astype("category")
    return df_copy


def main():
    df = pd.DataFrame({
        "age": [5, 70, 33, 41],
        "city": ["Pune", "Pune", "Delhi", "Pune"],
        "score": [1.5, 2.25, None, 4.0],
    })
    df = pd.concat([df] * 3, ignore_index=True)
    print(df.dtypes.to_dict(), df.memory_usage(deep=True).sum())
    out = shrink(df)
    print(out.dtypes.to_dict(), out.memory_usage(deep=True).sum())


if __name__ == "__main__":
    main()
