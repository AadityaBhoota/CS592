def find_length(string):
    max_diff = 0
    count_0 = 0
    count_1 = 0
    diff = {}
    
    for i in range(len(string)):
        if string[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        if count_0 - count_1 in diff:
            max_diff = max(max_diff, i - diff[count_0 - count_1])
        else:
            diff[count_0 - count_1] = i

    return max_diff

# Test cases




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)