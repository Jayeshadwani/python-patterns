from typing import Any, List, Optional


def add_item(item: Any, items: Optional[List[Any]] = None) -> List[Any]:
    """Append item to items and return items. BUGGY: fix the default argument."""
    if items is None:
        items = []
    items.append(item)
    return items


def main():
    items = []
    print("add_item(1) =", add_item(1, items))
    print("add_item(2) =", add_item(2, items))


if __name__ == "__main__":
    main()
