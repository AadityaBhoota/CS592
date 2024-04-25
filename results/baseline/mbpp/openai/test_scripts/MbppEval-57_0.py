def find_Max_Num(arr):
    # Sort the digits in descending order
    arr.sort(reverse=True)
    
    # Join the sorted digits to form the largest number
    num = int(''.join(map(str, arr)))
    
    return num

# Test examples




def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)