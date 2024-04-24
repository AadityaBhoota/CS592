def find_Max_Num(arr, n):
    """
    Find the largest number that can be formed with the given list of digits.

    Args:
    arr (list): A list of digits.
    n (int): The number of digits in the list.

    Returns:
    int: The largest number that can be formed with the given list of digits.
    """
    # Convert the list of digits to a list of strings
    digits = [str(d) for d in arr]

    # Sort the list of strings in descending order
    digits.sort(reverse=True)

    # Concatenate the sorted strings to form the largest number
    result = ''.join(digits)

    return int(result)

def check(candidate):
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([4,5,6,1]) == 6541
    assert find_Max_Num([1,2,3,9]) == 9321

check(find_Max_Num)