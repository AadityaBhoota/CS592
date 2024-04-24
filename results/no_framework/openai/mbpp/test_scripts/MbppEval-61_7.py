from collections import defaultdict

def count_substrings(s):
    def get_sum(num_str):
        return sum(int(digit) for digit in num_str)

    count = 0
    sum_to_count = defaultdict(int)
    sum_to_count[0] = 1
    cumulative_sum = 0

    for digit in s:
        cumulative_sum += int(digit)
        diff = cumulative_sum - len(str(count))
        count += sum_to_count[diff]
        sum_to_count[cumulative_sum] += 1

    return count

# Test cases
assert count_substrings('112112') == 6
assert count_substrings('111') == 6
assert count_substrings('1101112') == 12

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)