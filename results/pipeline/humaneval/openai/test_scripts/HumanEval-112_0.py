def reverse_delete(s, c):
    def remove_characters(s, c):
        return "".join(char for char in s if char not in c)

    def is_palindrome(s):
        return s == s[::-1]

    modified_s = remove_characters(s, c)
    is_palindrome_result = is_palindrome(modified_s)

    return modified_s, is_palindrome_result

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