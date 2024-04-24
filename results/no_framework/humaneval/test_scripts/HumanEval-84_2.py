def solve(N):
    # Convert the integer N to its binary representation
    binary_str = bin(N)[2:]
    
    # Calculate the sum of digits in binary
    sum_binary = str(bin(sum(int(digit) for digit in binary_str)))[2:]
    
    return sum_binary

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