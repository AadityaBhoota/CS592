def number_of_substrings(s):
    """
    Counts the number of non-empty substrings of a given string.
    
    Args:
        s (str): The input string.
        
    Returns:
        int: The number of non-empty substrings.
    """
    # Calculate the length of the input string
    n = len(s)
    
    # Use the formula n * (n + 1) // 2 to calculate the total number of substrings
    # This formula works because the number of substrings of length k is (n - k + 1)
    # and the sum of these for all k from 1 to n is n * (n + 1) // 2
    return n * (n + 1) // 2

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)