def validate(n):
    """
    Checks whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Args:
        n (int): The input integer.

    Returns:
        bool: True if the condition is met, False otherwise.
    """
    # Convert the integer to a string
    n_str = str(n)

    # Count the frequency of each digit
    digit_freq = {}
    for digit in n_str:
        if digit in digit_freq:
            digit_freq[digit] += 1
        else:
            digit_freq[digit] = 1

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