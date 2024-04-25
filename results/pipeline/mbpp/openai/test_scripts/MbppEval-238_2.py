def number_of_substrings(str):
    count = 0
    
    n = len(str)
    
    for i in range(n):
        for j in range(i, n):
            count += 1
    
    return count

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)