def reverse_delete(s, c):
    """
    Task:
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c,
    then check if the result string is a palindrome.
    A string is called a palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.

    Example:
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b", the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """
    # Create a set of characters in c for efficient lookup
    char_set = set(c)
    
    # Build the result string by filtering out the characters in s that are in c
    result = ''.join(char for char in s if char not in char_set)
    
    # Check if the result string is a palindrome
    is_palindrome = result == result[::-1]
    
    return (result, is_palindrome)

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