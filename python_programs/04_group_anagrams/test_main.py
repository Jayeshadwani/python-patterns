from main import group_anagrams


def test_basic():
    assert group_anagrams(["ab", "ba", "c"]) == [["ab", "ba"], ["c"]]


def test_classic():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]


def test_empty_list():
    assert group_anagrams([]) == []


def test_empty_string():
    assert group_anagrams([""]) == [[""]]


def test_single_word():
    assert group_anagrams(["a"]) == [["a"]]


def test_duplicates_kept():
    assert group_anagrams(["abc", "bca", "cab", "abc"]) == [["abc", "bca", "cab", "abc"]]


def test_case_sensitive():
    assert group_anagrams(["Ab", "bA", "ab"]) == [["Ab", "bA"], ["ab"]]


def test_same_letters_different_counts():
    assert group_anagrams(["aab", "abb"]) == [["aab"], ["abb"]]