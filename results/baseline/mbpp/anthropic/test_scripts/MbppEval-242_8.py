def count_charac(str1):
    """
    Counts the total number of characters in a given string.

    Args:
        str1 (str): The input string.

    Returns:
        int: The total number of characters in the input string.
    """
    return len(str1)

def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5

check(count_charac)