def decimal_to_binary(decimal):
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove the '0b' prefix
    binary = '0' * (8 - len(binary) % 8) + binary if len(binary) % 8 != 0 else binary  # Pad with zeros to make it a multiple of 8
    
    binary = 'db' + binary + 'db'  # Add 'db' at the beginning and end
    
    return binary

def check(candidate):

    # Check some simple cases
    assert candidate(0) == "db0db"
    assert candidate(32) == "db100000db"
    assert candidate(103) == "db1100111db"
    assert candidate(15) == "db1111db", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(decimal_to_binary)