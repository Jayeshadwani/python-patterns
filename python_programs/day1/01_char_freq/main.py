def char_freq(string):
    """
    This function takes a string as input and returns a dictionary with the frequency of each character in the string.
    
    :param string: The input string
    :return: A dictionary with characters as keys and their frequencies as values
    """
    freq_dict = {}
    for char in string:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

assert char_freq("aab") == {'a': 2, 'b': 1}
assert char_freq("") == {}

def main():
    test_string = "hello world"
    frequency = char_freq(test_string)
    print(f"Character frequency in '{test_string}': {frequency}")

if __name__ == "__main__":
    main()  