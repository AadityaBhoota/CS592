def min_Swaps(str1, str2):
    # Count the number of 1s and 0s in both strings
    count_1_str1 = str1.count('1')
    count_1_str2 = str2.count('1')
    count_0_str1 = len(str1) - count_1_str1
    count_0_str2 = len(str2) - count_1_str2

    # Check if both strings have the same number of ones and zeros
    if count_1_str1 != count_1_str2 or count_0_str1 != count_0_str2:
        return "Not Possible"

    # Count the number of mismatches (number of bits that are different)
    mismatches = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            mismatches += 1

    # To convert one binary number to another, we need half the mismatches number of swaps
    return mismatches // 2

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)