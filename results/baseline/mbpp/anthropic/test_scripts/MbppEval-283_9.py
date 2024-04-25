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

    # Create a dictionary to store the frequency of each digit
    digit_freq = {}

    # Count the frequency of each digit
    for digit in n_str:
        digit_freq[digit] = digit_freq.get(digit, 0) + 1

    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit, freq in digit_freq.items():
        if freq > int(digit):
            return False

    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)