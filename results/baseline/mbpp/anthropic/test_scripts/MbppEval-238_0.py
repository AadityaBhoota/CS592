def number_of_substrings(s):
    """
    Count the number of non-empty substrings of a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of non-empty substrings.
    """
    n = len(s)
    return (n * (n + 1)) // 2

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)