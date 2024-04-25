def min_Swaps(str1, str2):
    """
    Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.

    Examples:
    min_Swaps("1101", "1110") == 1
    min_Swaps("111", "000") == "Not Possible"
    min_Swaps("111", "110") == "Not Possible"
    """
    if len(str1) != len(str2):
        return "Not Possible"

    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1

    if diff_count % 2 != 0:
        return "Not Possible"

    swaps = 0
    for i in range(len(str1) - 1):
        if str1[i] != str2[i]:
            for j in range(i + 1, len(str1)):
                if str1[j] != str2[j]:
                    str1 = str1[:i] + str1[j] + str1[i + 1:j] + str1[i] + str1[j + 1:]
                    swaps += 1
                    break
    return swaps

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)