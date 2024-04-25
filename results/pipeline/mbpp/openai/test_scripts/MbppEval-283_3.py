def validate(n): 
    '''
    Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Examples:
    validate(1234) == True
    validate(51241) == False
    validate(321) == True
    '''
    n_str = str(n)  # Convert the integer n to a string
    result = True   # Assume the result is True initially
    
    for digit in n_str:  # Iterate through each digit in the string
        digit_count = n_str.count(digit)  # Count the frequency of each digit
        if digit_count > int(digit):  # Check if the frequency is greater than the digit itself
            result = False
            break  # Exit the loop if a digit violates the condition
    
    return result

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)