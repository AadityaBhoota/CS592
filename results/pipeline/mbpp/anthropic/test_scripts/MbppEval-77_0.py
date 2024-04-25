def is_Diff(n): 
    '''
    Write a python function to find whether a number is divisible by 11.

    Examples:
    is_Diff (12345) == False
    is_Diff(1212112) == True
    is_Diff(1212) == False
    '''
def is_divisible_by_11(n):
    """
    Write a python function to find whether a number is divisible by 11.

    Examples:
    is_divisible_by_11(12345) == False
    is_divisible_by_11(1212112) == True
    is_divisible_by_11(1212) == False
    """
    # Convert the input number to a string
    num_str = str(n)
    
    # Calculate the sum of digits at even positions and odd positions
    even_sum = sum(int(num_str[i]) for i in range(0, len(num_str), 2))
    odd_sum = sum(int(num_str[i]) for i in range(1, len(num_str), 2))
    
    # Calculate the difference between the two sums
    diff = even_sum - odd_sum
    
    # Check if the difference is 0 or a multiple of 11
    return diff == 0 or diff % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)