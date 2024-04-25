def reverse_delete(s, c):
    """
    Task:
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.

    Example:
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b", the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """
    # Create a set of characters to be removed
    remove_chars = set(c)

    # Build the new string by removing the characters
    new_string = ''.join(char for char in s if char not in remove_chars)

    # Check if the new string is a palindrome
    is_palindrome = new_string == new_string[::-1]

    return (new_string, is_palindrome)

def check(candidate):

    assert candidate("abcde","ae") == ('bcd',False)
    assert candidate("abcdef", "b") == ('acdef',False)
    assert candidate("abcdedcba","ab") == ('cdedc',True)
    assert candidate("dwik","w") == ('dik',False)
    assert candidate("a","a") == ('',True)
    assert candidate("abcdedcba","") == ('abcdedcba',True)
    assert candidate("abcdedcba","v") == ('abcdedcba',True)
    assert candidate("vabba","v") == ('abba',True)
    assert candidate("mamma", "mia") == ("", True)

check(reverse_delete)