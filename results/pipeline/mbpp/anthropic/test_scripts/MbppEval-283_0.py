def validate(n):
    """
    Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Examples:
    validate(1234) == True
    validate(51241) == False
    validate(321) == True
    """
    # Initialize a list to store the counts of each digit (0-9)
    digit_counts = [0] * 10
    
    # Extract the digits and update the counts
    while n > 0:
        digit = n % 10
        digit_counts[digit] += 1
        n //= 10
    
    # Check if the count of each digit is less than or equal to the digit itself
    for i in range(10):
        if digit_counts[i] > i:
            return False
    
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)