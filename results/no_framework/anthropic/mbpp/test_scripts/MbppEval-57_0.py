def find_Max_Num(arr, n):
    """
    Write a python function to find the largest number that can be formed with the given list of digits.

    Examples:
    find_Max_Num([1,2,3],3) == 321
    find_Max_Num([4,5,6,1],4) == 6541
    find_Max_Num([1,2,3,9],4) == 9321
    """
    # Convert the list of digits to a string
    digits_str = ''.join(map(str, arr))
    
    # Sort the digits in descending order
    sorted_digits = sorted(digits_str, reverse=True)
    
    # Join the sorted digits to form the largest number
    largest_num = ''.join(sorted_digits)
    
    return int(largest_num)

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)