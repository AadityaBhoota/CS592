def min_Swaps(str1, str2):
    if str1.count('1') != str2.count('1') or str1.count('0') != str2.count('0'):
        return "Not Possible"

    swaps = 0
    idx1, idx2 = len(str1) - 1, len(str2) - 1

    while idx1 >= 0 and idx2 >= 0:
        if str1[idx1] != str2[idx2]:
            swaps += 1
        idx1 -= 1
        idx2 -= 1

    return swaps

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)