def find_Max_Num(arr, n):
    sorted_arr = sorted(arr, reverse=True)
    result = 0
    for i in range(n):
        result = result * 10 + sorted_arr[i]
    return result

# Test cases




def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)