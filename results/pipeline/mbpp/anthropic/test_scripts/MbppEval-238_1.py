def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        count += len(s) - i
    return count

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)