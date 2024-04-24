def min_Swaps(str1, str2):
    if str1.count('1') != str2.count('1') or str1.count('0') != str2.count('0'):
        return "Not Possible"
    
    n = len(str1)
    swaps = 0
    
    i, j = 0, 0
    while i < n:
        if str1[i] != str2[j]:
            swaps += 1
        i += 1
        j += 1
    
    return swaps // 2

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)