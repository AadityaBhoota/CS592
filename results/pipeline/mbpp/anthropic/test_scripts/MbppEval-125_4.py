def find_length(string):
    max_diff = 0
    count_0 = 0
    count_1 = 0
    
    for char in string:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        current_diff = abs(count_0 - count_1)
        max_diff = max(max_diff, current_diff)
    
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)