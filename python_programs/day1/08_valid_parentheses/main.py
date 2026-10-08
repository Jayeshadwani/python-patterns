def is_valid(s: str) -> bool:
    """Return True if all brackets in s are closed by the same type, in correct order."""
    # Key-value pairs to match the brackets
    pairs = {
        "(": ")",
        "[" : "]",
        "{" : "}"
    }
    
    stack = []
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        else:
            # closing before opening, stack is empty
            if len(stack) == 0:
                return False
            open_bracket = stack.pop()
            if not pairs[open_bracket] == bracket:
                return False
    
    # At the end, stack should be empty so every possible pair is matched.
    if len(stack) == 0:
        return True
    return False



def main():
    for s in ["()", "([)]", "{[]}"]:
        print(f"is_valid({s!r}) = {is_valid(s)}")


if __name__ == "__main__":
    main()