def find_Max_Num(arr):
    # Sort the list of digits in descending order
    arr.sort(reverse=True)
    
    # Convert the list of digits to a string and then to an integer
    max_num = int(''.join(map(str, arr)))
    
    return max_num

# Test cases




def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)