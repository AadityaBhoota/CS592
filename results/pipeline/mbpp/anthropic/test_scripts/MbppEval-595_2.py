def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"

    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1

    if diff_count % 2 != 0:
        return "Not Possible"

    return diff_count // 2

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)