def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"
    
    if str1.count('1') != str2.count('1') or str1.count('0') != str2.count('0'):
        return "Not Possible"
    
    swaps = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            swaps += 1
            
    return swaps // 2

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)