def is_Diff(n):
    """
    Write a python function to find whether a number is divisible by 11.

    Examples:
    is_Diff(12345) == False
    is_Diff(1212112) == True
    is_Diff(1212) == False
    """
    # Convert the number to a string and get the length
    n_str = str(n)
    n_len = len(n_str)

    # Initialize the difference
    diff = 0

    # Iterate through the digits, alternating the sign
    for i in range(n_len):
        if i % 2 == 0:
            diff += int(n_str[i])
        else:
            diff -= int(n_str[i])

    # Check if the difference is divisible by 11
    return diff % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)