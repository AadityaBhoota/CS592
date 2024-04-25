def find_Max_Num(arr):
    result = ""
    
    arr.sort(reverse=True)
    
    result = ''.join(map(str, arr))
    
    result = int(result)
    return result

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)