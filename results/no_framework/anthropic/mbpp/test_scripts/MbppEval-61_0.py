from collections import defaultdict

def count_Substrings(s):
    n = len(s)
    count = 0
    dp = defaultdict(int)

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += int(s[j])
            if total == j - i + 1:
                count += 1
            dp[total] += 1

    return count

# Examples




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)