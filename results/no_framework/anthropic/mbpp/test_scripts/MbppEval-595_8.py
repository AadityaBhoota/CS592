def min_Swaps(str1, str2):
    """
    Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.

    Examples:
    min_Swaps("1101","1110") == 1
    min_Swaps("111","000") == "Not Possible"
    min_Swaps("111","110") == "Not Possible"
    """
    if len(str1) != len(str2):
        return "Not Possible"

    # Count the number of bits that need to be swapped
    diff_count = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)

    # If the total number of different bits is odd, it's not possible to convert
    if diff_count % 2 != 0:
        return "Not Possible"

    return diff_count // 2

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)