def find_Max_Num(arr):
    str_arr = [str(num) for num in arr]
    sorted_str_arr = sorted(str_arr, reverse=True)
    final_num = int("".join(sorted_str_arr))
    return final_num

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)