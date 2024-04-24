from collections import defaultdict

def count_Substrings(s):
    """
    Write a Python function to count the number of substrings with the sum of digits equal to their length.

    Examples:
    count_Substrings('112112', 6) == 6
    count_Substrings('111', 3) == 6
    count_Substrings('1101112', 7) == 12
    """
    n = len(s)
    count = 0

    for length in range(1, n + 1):
        digit_sum = 0
        for i in range(n - length + 1):
            substr = s[i:i + length]
            for char in substr:
                digit_sum += int(char)
            if digit_sum == length:
                count += 1
            digit_sum = 0

    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)