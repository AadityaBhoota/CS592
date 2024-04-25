def reverse_delete(s, c):
    c_set = set(c)
    new_s = ''.join(char for char in s if char not in c_set)
    is_palindrome = new_s == new_s[::-1]
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