def number_of_substrings(s):
    count = 0
    n = len(s)
    count = n * (n + 1) // 2
    for i in range(n):
        for j in range(i + 1, n + 1):
            count += 1
    return count

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)