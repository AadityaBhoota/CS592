def min_Swaps(str1, str2):
    # Check if the length of both strings is not the same
    if len(str1) != len(str2):
        return "Not Possible"

    # Count number of differences between str1 and str2
    diff_count = sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
    
    # If there are more than 2 differences, it is not possible to convert one string to another
    if diff_count > 2:
        return "Not Possible"
    
    # If there is exactly 1 difference, 1 swap is enough
    if diff_count == 1:
        return 1
    
    # If there are exactly 2 differences, we need 1 or 2 swaps to convert the strings
    # Return the minimum of 1 and 2
    return min(1, diff_count)

# Test the function with examples




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)