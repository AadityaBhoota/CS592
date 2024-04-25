from collections import defaultdict

def count_Substrings(s):
    digit_counts = defaultdict(int)
    running_sum = 0

    for char in s:
        running_sum += int(char)
        digit_counts[running_sum] += 1

    return sum(digit_counts.values())

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)