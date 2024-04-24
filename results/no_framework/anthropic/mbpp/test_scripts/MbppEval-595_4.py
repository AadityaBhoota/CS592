def min_Swaps(str1, str2):
    """
    Write a Python function to count the minimum number of swaps required to convert one binary number represented as a string to another.

    Examples:
    min_Swaps("1101", "1110") == 1
    min_Swaps("111", "000") == "Not Possible"
    min_Swaps("111", "110") == "Not Possible"
    """
    # Check if the strings have the same length
    if len(str1) != len(str2):
        return "Not Possible"

    # Count the number of bits that need to be swapped
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1

    # If the number of different bits is odd, it's not possible to convert
    if diff_count % 2 != 0:
        return "Not Possible"

    return diff_count // 2

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)