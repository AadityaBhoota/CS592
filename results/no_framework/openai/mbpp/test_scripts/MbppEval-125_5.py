def find_length(string):
    n = len(string)
    diff = 0  # Initialize the maximum difference to be 0
    count_0 = 0
    count_1 = 0
    count_diff = {0: -1}  # Store the index where the difference occurred

    for i in range(n):
        if string[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

        curr_diff = count_0 - count_1

        if curr_diff in count_diff:
            diff = max(diff, i - count_diff[curr_diff])
        else:
            count_diff[curr_diff] = i

    return diff

# Test cases




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)