def number_of_substrings(string):
    """
    Write a python function to count the number of non-empty substrings of a given string.

    Examples:
    number_of_substrings("abc") == 6
    number_of_substrings("abcd") == 10
    number_of_substrings("abcde") == 15
    """
    n = len(string)
    return n * (n + 1) // 2

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)