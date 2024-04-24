def count_set_bits(n): 
    count = 0
    while n: 
        count += n & 1
        n >>= 1
    return count

def min_Swaps(str1, str2):
    count_1 = count_set_bits(int(str1, 2))
    count_2 = count_set_bits(int(str2, 2))

    if abs(count_1 - count_2) % 2 != 0:
        return "Not Possible"

    swaps = 0
    diff = count_1 - count_2
    flag = diff > 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if diff > 0:
                diff -= 1
                if flag: swaps += 1
            else:
                diff += 1
                if not flag: swaps += 1

    return swaps

# Test cases




def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)