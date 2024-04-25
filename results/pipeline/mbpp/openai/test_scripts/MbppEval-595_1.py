def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"

    swaps_count = 0

    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            swaps_count += 1
    
    if swaps_count % 2 != 0:
        return "Not Possible"
    
    return swaps_count

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)