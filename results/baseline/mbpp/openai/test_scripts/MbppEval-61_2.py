from collections import defaultdict

def count_Substrings(s, n):
    cnt = 0
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    cur_sum = 0

    for i in range(len(s)):
        cur_sum += int(s[i])
        for j in range(1, min(i + 1, n) + 1):
            if cur_sum - j >= 0:
                cnt += prefix_sums[cur_sum - j]

        prefix_sums[cur_sum] += 1

    return cnt

# Test cases




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)