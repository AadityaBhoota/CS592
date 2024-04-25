def reverse_delete(s, c):
    def delete_chars_from_string(s, chars_to_delete):
        result = ""
        for char in s:
            if char not in chars_to_delete:
                result += char
        return result

    def is_palindrome(s):
        return s == s[::-1]
    
    result_string = delete_chars_from_string(s, c)
    is_palindrome_result = is_palindrome(result_string)

    return result_string, is_palindrome_result

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