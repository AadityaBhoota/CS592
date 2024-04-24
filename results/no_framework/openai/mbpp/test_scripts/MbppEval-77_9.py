def is_Diff(n):
    '''
    Function to check if a number is divisible by 11.
    
    Args:
    n: integer - The number to check
    
    Returns:
    True if the number is divisible by 11, False otherwise
    '''
    # Convert the number to a string to iterate over its digits
    num_str = str(n)
    
    # Calculate the alternating sum of digits
    diff = 0
    for i in range(len(num_str)):
        diff += int(num_str[i]) * (-1)**i
    
    # Check if the difference is divisible by 11
    return diff % 11 == 0

# Test the function




def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)