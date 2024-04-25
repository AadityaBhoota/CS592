def find_length(string):
    max_diff = 0
    count_0 = 0
    count_1 = 0
    count_diff = {}
    
    for i in range(len(string)):
        if string[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        diff = count_0 - count_1
        if diff not in count_diff:
            count_diff[diff] = i
        else:
            max_diff = max(max_diff, i - count_diff[diff])
    
    return max_diff

# Testing the function with the provided examples
assert find_length("11000010001") == 6
assert find_length("10111") == 1
assert find_length("11011101100101") == 2



def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)