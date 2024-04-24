def reverse_delete(s, c):
    # Removing characters in s that are equal to any character in c
    result_string = ''.join([char for char in s if char not in c])
    
    # Checking if the result string is a palindrome
    is_palindrome = result_string == result_string[::-1]
    
    return (result_string, is_palindrome)

# Testing the function with examples
print(reverse_delete("abcde", "ae"))  # Expected output: ('bcd', False)
print(reverse_delete("abcdef", "b"))  # Expected output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # Expected output: ('cdedc', True)

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