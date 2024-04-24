def number_of_substrings(s):
    n = len(s)
    return int(n*(n+1)/2)

# Test the function with examples




def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)