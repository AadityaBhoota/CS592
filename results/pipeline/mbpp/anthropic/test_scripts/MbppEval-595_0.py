def min_Swaps(str1, str2):
    count1 = str1.count('1')
    count2 = str2.count('1')

    if count1 != count2:
        return "Not Possible"

    diff_positions = [i for i in range(len(str1)) if str1[i] != str2[i]]
    return len(diff_positions) // 2

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)