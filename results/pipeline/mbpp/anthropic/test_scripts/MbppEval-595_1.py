def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"
    
    diff = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)
    
    if diff % 2 != 0:
        return "Not Possible"
    
    return diff // 2

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)