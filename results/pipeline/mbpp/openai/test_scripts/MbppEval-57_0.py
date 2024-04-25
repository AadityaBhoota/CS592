def find_Max_Num(arr):
    str_arr = [str(x) for x in arr]  
    sorted_str = ''.join(sorted(str_arr, reverse=True))
    max_num = int(sorted_str)  
    return max_num

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)