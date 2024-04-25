def find_length(string):
    max_diff = 0
    current_diff = 0
    
    for char in string:
        if char == '1':
            current_diff += 1
        else:
            current_diff -= 1
        max_diff = max(max_diff, abs(current_diff))
    
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)