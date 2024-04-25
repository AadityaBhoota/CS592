def find_Max_Num(arr):
    # Convert the list of digits into a list of strings
    arr_str = [str(digit) for digit in arr]
    
    # Sort the list of strings in descending order
    arr_str.sort(reverse=True)
    
    # Concatenate the sorted strings to form the largest number
    largest_num = ''.join(arr_str)
    
    return int(largest_num)

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)