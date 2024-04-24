def solve(N):
    # Convert the integer N to its binary representation and then convert it to a string
    binary_str = bin(N)[2:]
    
    # Calculate the sum of digits of the binary number
    sum_of_digits = sum([int(digit) for digit in binary_str])
    
    # Convert the sum to binary representation and return it as a string
    return bin(sum_of_digits)[2:]

# Test the function




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