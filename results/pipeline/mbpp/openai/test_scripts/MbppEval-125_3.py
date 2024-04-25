def find_length(string):
    max_diff = 0
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            count_0 = 0
            count_1 = 0
            for k in range(i, j+1):
                if string[k] == '0':
                    count_0 += 1
                else:
                    count_1 += 1
            diff = abs(count_0 - count_1)
            if diff > max_diff:
                max_diff = diff

    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)