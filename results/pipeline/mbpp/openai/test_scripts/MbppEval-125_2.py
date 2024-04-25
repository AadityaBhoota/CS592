def find_length(string):
    max_diff = 0
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            substr = string[i:j+1]
            count_0 = substr.count('0')
            count_1 = len(substr) - count_0
            diff = abs(count_0 - count_1)
            max_diff = max(max_diff, diff)

    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)