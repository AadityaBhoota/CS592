def min_Swaps(str1, str2):
    """
    Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.

    Examples:
    min_Swaps("1101", "1110") == 1
    min_Swaps("111", "000") == "Not Possible"
    min_Swaps("111", "110") == "Not Possible"
    """
    # Check if the lengths of the two strings are equal
    if len(str1) != len(str2):
        return "Not Possible"

    # Count the number of bits that need to be flipped
    diff_count = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)

    # If the total number of bits that need to be flipped is odd, it's not possible
    if diff_count % 2 != 0:
        return "Not Possible"

    # Count the minimum number of swaps required
    swaps = diff_count // 2
    return swaps

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)