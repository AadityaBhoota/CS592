def solve(N):
    # Calculate the sum of digits in binary
    binary_sum = 0
    while N > 0:
        binary_sum += N % 2
        N //= 2
    
    # Convert the binary sum to a binary string
    binary_string = bin(binary_sum)[2:]
    
    return binary_string

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