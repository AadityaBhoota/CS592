def min_Swaps(str1, str2):
    if str1.count('1') != str2.count('1') or len(str1) != len(str2):
        return "Not Possible"
    
    swaps = 0
    i = 0
    j = 0
    
    while i < len(str1):
        if str1[i] != str2[j]:
            swaps += 1
        i += 1
        j += 1
        
    return swaps // 2

# Test Cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)