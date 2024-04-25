def find_Parity(x):
    """
    Write a python function to find whether the parity of a given number is odd.

    Examples:
    find_Parity(12) == "Even Parity"
    find_Parity(7) == "Odd Parity"
    find_Parity(10) == "Even Parity"
    """
    # Convert the number to binary string and count the number of set bits
    set_bits = bin(x).count("1")
    
    # Determine the parity based on the number of set bits
    if set_bits % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

def check(candidate):
    assert find_Parity(12) == False
    assert find_Parity(7) == True
    assert find_Parity(10) == False

check(find_Parity)