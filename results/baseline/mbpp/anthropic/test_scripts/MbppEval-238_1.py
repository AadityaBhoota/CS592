def number_of_substrings(s):
    """
    Count the number of non-empty substrings of a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of non-empty substrings.
    """
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += 1
    return count

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)