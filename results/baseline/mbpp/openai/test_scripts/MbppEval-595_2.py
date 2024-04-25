def min_Swaps(str1, str2):
    if str1.count('1') != str2.count('1'):
        return "Not Possible"

    swaps = 0
    ones_indices_str1 = [i for i in range(len(str1)) if str1[i] == '1']

    for i in range(len(str2)):
        if str2[i] == '1':
            if not ones_indices_str1:
                return "Not Possible"
            index = ones_indices_str1.pop(0)
            swaps += abs(index - i)

    return swaps

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)