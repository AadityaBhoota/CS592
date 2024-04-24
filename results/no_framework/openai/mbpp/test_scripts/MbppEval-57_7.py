def find_Max_Num(arr):
    arr.sort(reverse=True)  # Sort the array in descending order
    return int(''.join(map(str, arr)))

# Test cases




def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)