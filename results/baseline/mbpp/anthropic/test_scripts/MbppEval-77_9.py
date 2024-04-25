def is_Diff(n):
    """
    Write a python function to find whether a number is divisible by 11.

    Examples:
    is_Diff(12345) == False
    is_Diff(1212112) == True
    is_Diff(1212) == False
    """
    # Convert the number to a string
    num_str = str(n)
    
    # Initialize the difference to 0
    diff = 0
    
    # Iterate through the digits of the number
    for i in range(len(num_str)):
        # Add the digit to the difference if the index is even, subtract if the index is odd
        if i % 2 == 0:
            diff += int(num_str[i])
        else:
            diff -= int(num_str[i])
    
    # Check if the difference is divisible by 11
    return diff % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)