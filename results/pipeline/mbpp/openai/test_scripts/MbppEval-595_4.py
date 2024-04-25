def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"
    
    swap_count = 0

    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            swap_count += 1
    
    if swap_count % 2 == 0:
        return swap_count // 2
    else:
        return "Not Possible"

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)