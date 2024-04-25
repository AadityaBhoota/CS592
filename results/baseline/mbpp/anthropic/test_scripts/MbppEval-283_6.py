def validate(n):
    """
    Write a Python function that takes an integer and checks whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Examples:
    validate(1234) == True
    validate(51241) == False
    validate(321) == True
    """
    # Convert the integer to a string to iterate over the digits
    n_str = str(n)

    # Create a dictionary to store the frequency of each digit
    freq = {}

    # Iterate over the digits and count their frequency
    for digit in n_str:
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1

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