def find_length(string):
    """
    Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.

    Examples:
    find_length("11000010001", 11) == 6
    find_length("10111", 5) == 1
    find_length("11011101100101", 14) == 2
    """
    max_diff = 0
    count = 0
    min_count = 0

    for char in string:
        if char == '0':
            count += 1
        else:
            count -= 1
        max_diff = max(max_diff, abs(count - min_count))
        min_count = min(min_count, count)

    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)