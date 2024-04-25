def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"
    
    swap_count = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            swap_count += 1
    
    return swap_count

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)