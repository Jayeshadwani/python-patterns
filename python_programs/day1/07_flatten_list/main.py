from typing import Any, List

def flatten_recursive_call(nested: List[Any],flattened_list: List[Any]):
    # base case
    if not isinstance(nested, List):
        return flattened_list.append(nested)
        
    for ele in nested:
        flatten_recursive_call(ele,flattened_list)    
    


def flatten(nested: List[Any]) -> List[Any]:
    """Return a flat list of all non-list items, in left-to-right order."""
    flattened_list = []
    
    flatten_recursive_call(nested,flattened_list)
    
    return flattened_list
    


def main():
    nested = [1, [2, [3]]]
    print(f"flatten({nested}) = {flatten(nested)}")


if __name__ == "__main__":
    main()