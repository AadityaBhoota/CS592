def find_Max_Num(arr, n):
    if not isinstance(arr, list) or not all(isinstance(digit, int) for digit in arr) or len(arr) != n:
        raise ValueError("Invalid input. The input should be a list of integers with length equal to the given 'n' value.")
    
    arr.sort(reverse=True)
    max_num = int(''.join(map(str, arr)))
    return max_num

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)