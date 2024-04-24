def find_length(string):
    max_diff = 0
    count_1 = 0
    count_0 = 0
    diff_dict = {0: -1}
    
    for i in range(len(string)):
        if string[i] == '1':
            count_1 += 1
        else:
            count_0 += 1
        
        diff = count_0 - count_1
        
        if diff in diff_dict:
            max_diff = max(max_diff, i - diff_dict[diff])
        else:
            diff_dict[diff] = i
    
    return max_diff

# Test the function with the given examples




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)