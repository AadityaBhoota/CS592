def find_length(string):
    zero_count = 0
    one_count = 0
    max_diff = 0
    
    for char in string:
        if char == '0':
            zero_count += 1
        else:
            one_count += 1
        
        diff = zero_count - one_count
        if diff > max_diff:
            max_diff = diff
        
        if diff < 0:
            zero_count = 0
            one_count = 0
    
    return max_diff

# Test cases




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)