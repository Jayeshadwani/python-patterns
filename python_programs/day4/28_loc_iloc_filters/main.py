import pandas as pd


def first_n(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """First n rows by position."""
    return df.iloc[:n]


def by_labels(df: pd.DataFrame, labels: list) -> pd.DataFrame:
    """Rows whose index label is in labels, in the given order. Missing label -> KeyError."""
    return df.loc[labels]


def filter_city_age(df: pd.DataFrame, city: str, min_age: int) -> pd.DataFrame:
    """Rows with df.city == city and df.age >= min_age; only columns name and age; index kept."""
    return df[(df.city == city) & (df.age >= min_age)][["name", "age"]]


def last_row_name(df: pd.DataFrame) -> str:
    """The 'name' of the last row by position."""
    return df.tail(1)["name"].values[0]


def main():
    df = pd.DataFrame({"name": ["Ana", "Ben", "Cleo", "Dev"],
                       "age": [34, 19, 41, 27],
                       "city": ["Pune", "Delhi", "Pune", "Pune"]},
                      index=[30, 10, 20, 40])
    print(first_n(df, 2))
    print(by_labels(df, [40, 10]))
    print(filter_city_age(df, "Pune", 30))
    print(last_row_name(df))


if __name__ == "__main__":
    main()
