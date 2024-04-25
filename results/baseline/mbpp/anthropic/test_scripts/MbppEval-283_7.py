def validate(n):
    """
    Checks whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Args:
        n (int): The integer to be validated.

    Returns:
        bool: True if the frequency of each digit is less than or equal to the digit itself, False otherwise.
    """
    # Convert the integer to a string
    n_str = str(n)

    # Create a dictionary to store the frequency of each digit
    freq = {}

    # Count the frequency of each digit
    for digit in n_str:
        freq[digit] = freq.get(digit, 0) + 1

    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit, count in freq.items():
        if count > int(digit):
            return False

    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)