def validate(n):
    """
    Write a python function that takes in an integer and checks whether the frequency of each digit in the integer is less than or equal to the digit itself.
    
    Examples:
    validate(1234) == True
    validate(51241) == False
    validate(321) == True
    """
    digit_count = {}
    
    while n > 0:
        digit = n % 10
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
        n //= 10
    
    for digit, count in digit_count.items():
        if count > digit:
            return False
    
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)