def validate(n):
    """
    Checks whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Args:
        n (int): The integer to be validated.

    Returns:
        bool: True if the frequency of each digit is less than or equal to the digit itself, False otherwise.
    """
    # Convert the integer to a string and iterate over each digit
    for digit in str(n):
        # Count the frequency of the current digit
        freq = str(n).count(digit)
        # Check if the frequency is less than or equal to the digit itself
        if freq > int(digit):
            return False
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)