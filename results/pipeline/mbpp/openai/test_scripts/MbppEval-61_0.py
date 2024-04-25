from collections import defaultdict

def count_Substrings(s):
    count = 0
    prefix_sums = defaultdict(int)

    for i in range(len(s)):
        digit = int(s[i])
        prefix_sums[i+1] = prefix_sums[i] + digit

        if prefix_sums[i+1] == (i+1):
            count += 1

    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)