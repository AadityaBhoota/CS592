def find_Max_Num(arr, n):
    arr.sort(reverse=True)
    largest_num = ''.join(map(str, arr))
    return int(largest_num)

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)