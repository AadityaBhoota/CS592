def reverse_delete(s, c):
    # Deleting characters in s that are equal to any character in c
    result = ''.join([char for char in s if char not in c])
    
    # Check if the result string is palindrome
    is_palindrome = result == result[::-1]
    
    return (result, is_palindrome)

# Test cases
print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
print(reverse_delete("abcdef", "b"))   # Output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)

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