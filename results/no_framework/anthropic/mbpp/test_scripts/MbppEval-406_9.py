def find_Parity(x):
    """
    Write a python function to find whether the parity of a given number is odd.

    Examples:
    find_Parity(12) == "Even Parity"
    find_Parity(7) == "Odd Parity"
    find_Parity(10) == "Even Parity"
    """
    if x & 1 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

def check(candidate):
    assert find_Parity(12) == False
    assert find_Parity(7) == True
    assert find_Parity(10) == False

check(find_Parity)