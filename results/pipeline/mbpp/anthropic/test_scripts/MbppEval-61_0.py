from collections import defaultdict

def count_Substrings(s):
    count = defaultdict(int)
    for i in range(len(s)):
        curr_sum = 0
        for j in range(i, len(s)):
            curr_sum += int(s[j])
            count[curr_sum] += 1
    return sum(count.values())

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)