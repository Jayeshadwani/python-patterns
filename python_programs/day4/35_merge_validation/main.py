import pandas as pd


def duplicate_keys(df: pd.DataFrame, key: str) -> list:
    """Sorted list of key values appearing more than once (missing ignored)."""
    duplicate_keys = {}
    duplicate_keys_l =[]
    
    for k in df[key]:
        if pd.isna(k):
            continue
        count = duplicate_keys.get(k,0) + 1

        # if count > 1: # count > 1? A key is appended exactly when it becomes a duplicate for the first time. This guarantees each duplicate key appears once.
        if count == 2:
            duplicate_keys_l.append(k)
        
        duplicate_keys[k] = count


    return sorted(duplicate_keys_l)


def row_growth(left: pd.DataFrame, right: pd.DataFrame, on: str, how: str = "left") -> float:
    """len(merged) / len(left); 1.0 if left is empty."""
    if len(left) == 0:
        return 1
    
    merged_df = pd.merge(left,right,on=on,how=how)

    return len(merged_df) / len(left)


def checked_merge(left: pd.DataFrame, right: pd.DataFrame, on: str,
                  how: str = "left", validate: str = "many_to_one") -> pd.DataFrame:
    """Merge with pandas validate; re-raise as ValueError with duplicate keys listed."""
    try:
        merged_df = pd.merge(left,right,on=on,how=how,validate=validate)
        return merged_df
    
    except pd.errors.MergeError as e:
            left_duplicates = duplicate_keys(left, on)
            right_duplicates = duplicate_keys(right, on)

            raise ValueError(
            f"validate={validate}; "
            f"left={left_duplicates}; "
            f"right={right_duplicates}"
        ) from e

    


def main():
    orders = pd.DataFrame({"order_id": [1, 2, 3, 4], "customer_id": [1, 2, 2, 3]})
    dirty = pd.DataFrame({"customer_id": [1, 2, 3, 2], "name": ["Ana", "Ben", "Cy", "Ben (old)"]})
    print(duplicate_keys(dirty, "customer_id"))
    print(row_growth(orders, dirty, "customer_id"))
    try:
        checked_merge(orders, dirty, "customer_id")
    except ValueError as e:
        print("ValueError:", e)


if __name__ == "__main__":
    main()
