def is_undulating(n):
    """
    Checks whether the given number is undulating or not.

    An undulating number is a number where the digits go up and down,
    up and down, and so on. For example, 1212121 is an undulating
    number, but 1991 is not.

    Args:
        n (str): The number to check.

    Returns:
        bool: True if the number is undulating, False otherwise.
    """
    # Convert the input to a string
    n_str = str(n)

    # Check if the length of the string is less than 2
    if len(n_str) < 2:
        return False

    # Initialize the direction to 0 (neutral)
    direction = 0

    # Iterate through the digits of the number
    for i in range(1, len(n_str)):
        # Check the direction of the current digit compared to the previous one
        if int(n_str[i]) > int(n_str[i-1]):
            if direction == -1:
                return False
            direction = 1
        elif int(n_str[i]) < int(n_str[i-1]):
            if direction == 1:
                return False
            direction = -1

    # If the loop completed without returning False, the number is undulating
    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)