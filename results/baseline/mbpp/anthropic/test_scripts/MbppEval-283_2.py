def validate(n):
    """
    Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Examples:
    validate(1234) == True
    validate(51241) == False
    validate(321) == True
    """
    # Convert the integer to a string
    n_str = str(n)

    # Count the frequency of each digit
    digit_counts = {}
    for digit in n_str:
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit, count in digit_counts.items():
        if count > int(digit):
            return False

    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)