from typing import Optional


def first_unique(s: str) -> Optional[str]:
    """Return the first character that appears exactly once in s, else None."""
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None


def main():
    test_string = "aabc"
    print(f"First unique in '{test_string}': {first_unique(test_string)}")


if __name__ == "__main__":
    main()