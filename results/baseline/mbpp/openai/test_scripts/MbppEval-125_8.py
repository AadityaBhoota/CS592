def find_length(s):
    n = len(s)
    count = 0
    max_diff = 0
    count_dict = {0: -1}
    
    for i in range(n):
        count += 1 if s[i] == '0' else -1
        
        if count in count_dict:
            max_diff = max(max_diff, i - count_dict[count])
        else:
            count_dict[count] = i
        
    return max_diff

# Test cases




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)