def find_length(string): 
    max_diff = 0
    count = 0
    seen = {0: -1}
    
    for i, s in enumerate(string): 
        if s == '0': 
            count -= 1
        else: 
            count += 1
        
        if count in seen: 
            max_diff = max(max_diff, i - seen[count])
        else: 
            seen[count] = i
    
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)