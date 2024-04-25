def number_of_substrings(string):
    length = len(string)
    return int(length * (length + 1) / 2)

# Test cases




def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)