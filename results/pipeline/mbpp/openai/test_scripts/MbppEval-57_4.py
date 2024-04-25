def find_Max_Num(arr):
    arr_str = [str(num) for num in arr]
    arr_str.sort(key=lambda x: x*3, reverse=True)
    max_num_str = ''.join(arr_str)
    return int(max_num_str)

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)