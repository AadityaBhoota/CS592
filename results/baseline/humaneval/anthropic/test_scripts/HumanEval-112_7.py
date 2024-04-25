def reverse_delete(s, c):
    # Create a set of characters in c for efficient lookup
    chars_to_delete = set(c)

    # Create a new string by iterating through s and excluding the characters in c
    new_s = ''.join(char for char in s if char not in chars_to_delete)

    # Check if the new string is a palindrome
    is_palindrome = new_s == new_s[::-1]

    # Return the new string and the palindrome check result as a tuple
    return (new_s, is_palindrome)

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