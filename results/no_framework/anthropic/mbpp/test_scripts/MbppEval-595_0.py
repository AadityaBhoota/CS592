def min_Swaps(str1, str2):
    """
    Write a Python function to count the minimum number of swaps required to convert one binary number represented as a string to another.

    Examples:
    min_Swaps("1101", "1110") == 1
    min_Swaps("111", "000") == "Not Possible"
    min_Swaps("111", "110") == "Not Possible"
    """
    if len(str1) != len(str2):
        return "Not Possible"

    # Count the number of bits that need to be flipped
    diff = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)

    # If the total number of bits that need to be flipped is odd, it's not possible
    if diff % 2 != 0:
        return "Not Possible"

    # Count the minimum number of swaps required
    swaps = 0
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            j = i + 1
            while j < len(str1) and str1[j] != str2[i]:
                j += 1
            if j == len(str1):
                return "Not Possible"
            swaps += 1
            str1 = str1[:i] + str1[j] + str1[i+1:j] + str1[i] + str1[j+1:]
        i += 1

    return swaps

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)