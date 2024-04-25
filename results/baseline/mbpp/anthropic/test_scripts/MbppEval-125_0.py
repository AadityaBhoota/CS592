def find_length(string):
    """
    Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.

    Examples:
    find_length("11000010001", 11) == 6
    find_length("10111", 5) == 1
    find_length("11011101100101", 14) == 2
    """
    n = len(string)
    max_diff = 0

    for i in range(n):
        count_0 = 0
        count_1 = 0
        for j in range(i, n):
            if string[j] == '0':
                count_0 += 1
            else:
                count_1 += 1
            max_diff = max(max_diff, abs(count_0 - count_1))

    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)