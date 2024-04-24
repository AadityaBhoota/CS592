def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Not Possible"

    # Count the number of bits that are different
    diff_count = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)

    # If the number of different bits is odd, it's not possible to convert
    if diff_count % 2 != 0:
        return "Not Possible"

    # If the number of different bits is even, the minimum number of swaps is diff_count // 2
    return diff_count // 2

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)