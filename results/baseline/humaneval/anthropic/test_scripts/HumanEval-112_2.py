def reverse_delete(s, c):
    # Create a set of characters to be deleted
    chars_to_delete = set(c)
    
    # Create a new string by removing the characters to be deleted
    new_string = ''.join(char for char in s if char not in chars_to_delete)
    
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