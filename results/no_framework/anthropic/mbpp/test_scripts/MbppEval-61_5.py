from collections import defaultdict

def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += int(s[j])
            if curr_sum == j-i+1:
                count += 1
    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)