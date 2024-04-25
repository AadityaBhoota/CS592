from collections import defaultdict

def count_Substrings(s, n):
    """
    Count the number of substrings with the sum of digits equal to their length.

    Args:
    s: str, the input string
    n: int, the length of the input string

    Returns:
    int, the count of substrings with the sum of digits equal to their length
    """

    def count_digits(num):
        return sum(int(digit) for digit in str(num))

    count = 0
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    current_sum = 0

    for i in range(n):
        current_sum += int(s[i])
        count += prefix_sum[current_sum - i - 1]
        prefix_sum[current_sum] += 1

    return count

# Test cases




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)