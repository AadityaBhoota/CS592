def reverse_delete(s, c):
    # Remove characters in s that are equal to any character in c
    s_without_c = ''.join(char for char in s if char not in c)
    
    # Check if the result string is a palindrome
    is_palindrome = s_without_c == s_without_c[::-1]
    
    return s_without_c, is_palindrome

# Test the function with the given examples




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