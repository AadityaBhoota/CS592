def find_length(string, n):
    max_diff = 0
    current_diff = 0
    zeros = 0
    ones = 0
    
    for char in string:
        if char == '0':
            zeros += 1
        else:
            ones += 1
        current_diff = abs(zeros - ones)
        max_diff = max(max_diff, current_diff)
    
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)