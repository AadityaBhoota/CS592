from collections import defaultdict

def count_Substrings(s):
    """
    Write a python function to count the number of substrings with the sum of digits equal to their length.

    Examples:
    count_Substrings('112112',6) == 6
    count_Substrings('111',3) == 6
    count_Substrings('1101112',7) == 12
    """
    n = len(s)
    count = 0
    digit_sum = defaultdict(int)
    digit_sum[0] = 1  # Initialize the count for substrings with sum 0 to 1

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += int(s[j])
            if current_sum == j - i + 1:
                count += digit_sum[current_sum]
                digit_sum[current_sum] += 1

    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)