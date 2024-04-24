def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"

    zeros_str1 = 0
    ones_str1 = 0
    for i in range(len(str1)):
        if str1[i] == '0':
            zeros_str1 += 1
        else:
            ones_str1 += 1

    zeros_str2 = 0
    ones_str2 = 0
    for i in range(len(str2)):
        if str2[i] == '0':
            zeros_str2 += 1
        else:
            ones_str2 += 1

    if zeros_str1 != zeros_str2 or ones_str1 != ones_str2:
        return "Not Possible"

    swap_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            swap_count += 1

    return swap_count // 2

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)