from collections import defaultdict

def count_Substrings(s):
    n = len(s)
    count = 0
    digit_sum = [0] * (n + 1)

    # Compute the prefix sum of the digit sums
    for i in range(n):
        digit_sum[i + 1] = digit_sum[i] + int(s[i])

    # Use a dictionary to keep track of the count of substrings
    # with the sum of digits equal to their length
    dp = defaultdict(int)
    dp[0] = 1  # Empty string also satisfies the condition

    for i in range(1, n + 1):
        count += dp[digit_sum[i] - i]
        dp[digit_sum[i] - i] += 1

    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)