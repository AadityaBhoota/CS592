def solve(N):
    # Convert the integer to binary string and remove the '0b' prefix
    binary_str = bin(N)[2:]
    
    # Sum the digits of the binary string by converting each digit to int and summing them up
    total_sum = sum(int(digit) for digit in binary_str)
    
    # Convert the total sum back to binary string
    return bin(total_sum)[2:]

# Test cases




def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1000) == "1", "Error"
    assert candidate(150) == "110", "Error"
    assert candidate(147) == "1100", "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(333) == "1001", "Error"
    assert candidate(963) == "10010", "Error"


check(solve)