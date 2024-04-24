def validate(n):
    """
    Write a python function that takes in an integer and checks whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Examples:
    validate(1234) == True
    validate(51241) == False
    validate(321) == True
    """
    # Convert the integer to a string
    num_str = str(n)

    # Initialize a dictionary to store the frequency of each digit
    freq_dict = {}

    # Iterate through the digits in the number
    for digit in num_str:
        # Increment the frequency of the current digit
        freq_dict[digit] = freq_dict.get(digit, 0) + 1

        # Check if the frequency of the current digit is greater than the digit itself
        if freq_dict[digit] > int(digit):
            return False

    # If all digits pass the check, return True
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)