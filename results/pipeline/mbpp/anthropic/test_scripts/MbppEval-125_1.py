def find_length(string, n):
    max_diff = 0

    for i in range(n):
        num_0 = 0
        num_1 = 0
        for j in range(i, n):
            if string[j] == '0':
                num_0 += 1
            else:
                num_1 += 1
            curr_diff = abs(num_0 - num_1)
            max_diff = max(max_diff, curr_diff)

    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)