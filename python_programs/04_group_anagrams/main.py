from typing import List

def group_anagrams(words: List[str]) -> List[List[str]]:
    groups = {}
    for w in words:
        groups.setdefault("".join(sorted(w)), []).append(w)
    return list(groups.values())

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"group_anagrams({words}) = {group_anagrams(words)}")


if __name__ == "__main__":
    main()