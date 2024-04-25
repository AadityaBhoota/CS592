def min_Swaps(str1, str2):
    if str1.count('1') != str2.count('1') or str1.count('0') != str2.count('0'):
        return "Not Possible"

    swap_count = 0
    str1_idx = 0
    str2_idx = 0

    while str1_idx < len(str1):
        if str1[str1_idx] != str2[str2_idx]:
            swap_count += 1
        str1_idx += 1
        str2_idx += 1

    return swap_count

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)