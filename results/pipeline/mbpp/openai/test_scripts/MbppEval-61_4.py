from collections import defaultdict
def count_Substrings(s):
    '''
    Write a python function to count the number of substrings with the sum of digits equal to their length.

    Examples:
    count_Substrings('112112',6) == 6
    count_Substrings('111',3) == 6
    count_Substrings('1101112',7) == 12
    '''
def get_substrings(s):
    substrings = []
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substrings.append(s[start:end])
    return substrings

def get_digit_sum(s):
    return sum(int(d) for d in s if d.isdigit())

def count_substrings(s):
    substrings = get_substrings(s)
    count = 0
    for substring in substrings:
        if len(substring) == get_digit_sum(substring):
            count += 1
    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)