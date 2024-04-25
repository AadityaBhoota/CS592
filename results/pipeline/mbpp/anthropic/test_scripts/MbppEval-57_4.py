def find_Max_Num(arr, n):
    digits_str = ''.join(map(str, arr))
    sorted_digits = sorted(digits_str, reverse=True)
    return int(''.join(sorted_digits))

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)