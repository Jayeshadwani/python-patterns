from typing import Dict


def merge_dicts(a: Dict[str, float], b: Dict[str, float]) -> Dict[str, float]:
    """Return a new dict with all keys of a and b; shared keys get the summed value."""
    new_dict = {}

    # dictionaries have unique keys, and maintains the insertion order
    keys = list(dict.fromkeys(list(a) + list(b)))
    
    for key in keys:
        value = a.get(key,0) + b.get(key,0)
        new_dict[key] = value
    
    return new_dict


def main():
    a, b = {"a": 1, "b": 2}, {"b": 3, "c": 4}
    print(f"merge_dicts({a}, {b}) = {merge_dicts(a, b)}")


if __name__ == "__main__":
    main()