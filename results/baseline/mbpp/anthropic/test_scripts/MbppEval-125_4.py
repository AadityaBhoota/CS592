def find_length(string):
    max_diff = 0
    curr_diff = 0
    for char in string:
        if char == '0':
            curr_diff += 1
        else:
            curr_diff -= 1
        max_diff = max(max_diff, abs(curr_diff))
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)