def find_length(string):
    max_diff = 0
    count_zero = 0
    count_one = 0
    
    for char in string:
        if char == '0':
            count_zero += 1
        else:
            count_one += 1
            
        diff = abs(count_zero - count_one)
        max_diff = max(max_diff, diff)
    
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)