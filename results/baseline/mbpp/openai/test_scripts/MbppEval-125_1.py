def find_length(string): 
    max_diff = 0
    count_0 = count_1 = 0
    diff_map = {0: -1}  # Initialize the difference map with 0 at index -1
    
    for idx, char in enumerate(string): 
        if char == '0': 
            count_0 += 1
        else: 
            count_1 += 1
        
        diff = count_0 - count_1
        if diff not in diff_map: 
            diff_map[diff] = idx
        else: 
            max_diff = max(max_diff, idx - diff_map[diff])
    
    return max_diff

# Test cases




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)