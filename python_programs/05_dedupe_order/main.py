from typing import Any, List


def dedupe(items: List[Any]) -> List[Any]:
    """Return a new list with duplicates removed, keeping first occurrences in order."""
    new_items = []
    items_check = {}
    for item in items:
        if item not in items_check:
            new_items.append(item)
            items_check[item] = "Seen"
        
    return new_items


def main():
    items = [3, 1, 3, 2]
    print(f"dedupe({items}) = {dedupe(items)}")


if __name__ == "__main__":
    main()