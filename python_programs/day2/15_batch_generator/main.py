from typing import Iterable, Iterator, List, TypeVar

T = TypeVar("T")

def batch(iterable: Iterable[T], n: int) -> Iterator[List[T]]:
    """Yield lists of up to n items from iterable, in order. Last list may be shorter."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    yield_list: List[T] = []
    for item in iterable:
        yield_list.append(item)
        if len(yield_list) == n:
            yield yield_list # Yield the current batch
            yield_list = []
    
    # Yield any remaining items in yield_list if it is not empty
    if yield_list:
        yield yield_list
    


def main():
    print(list(batch(range(1, 6), 2)))
    print(list(batch("abcde", 2)))


if __name__ == "__main__":
    main()