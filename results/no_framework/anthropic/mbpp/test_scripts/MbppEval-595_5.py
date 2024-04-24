def min_Swaps(str1, str2):
    """
    Write a python function to count the minimum number of swaps required to convert one binary number represented as a string to another.

    Examples:
    min_Swaps("1101", "1110") == 1
    min_Swaps("111", "000") == "Not Possible"
    min_Swaps("111", "110") == "Not Possible"
    """
    if len(str1) != len(str2):
        return "Not Possible"

    # Count the number of bits that need to be swapped
    diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1

    # If the total number of bits that need to be swapped is odd, it's not possible
    if diff % 2 != 0:
        return "Not Possible"

    # Count the minimum number of swaps required
    return diff // 2

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)