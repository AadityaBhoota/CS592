from collections import defaultdict

def count_Substrings(s):
    count_dict = defaultdict(int)

    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j+i]
            if sum(int(digit) for digit in substring) == i:
                count_dict[i] += 1

    return sum(count_dict.values())

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)