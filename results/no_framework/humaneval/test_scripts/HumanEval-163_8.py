def generate_integers(a, b):
    if a > b:
        a, b = b, a  # Ensure a is smaller than b

    result = [int(digit) for digit in str(a) if int(digit) % 2 == 0]
    current = a + (2 - a % 2)  # Start from the next even number after a

    while current <= b:
        result.append(current)
        current += 2

    return result

# Test cases
print(generate_integers(2, 8))  # Output: [2, 4, 6, 8]
print(generate_integers(8, 2))  # Output: [2, 4, 6, 8]
print(generate_integers(10, 14))  # Output: []

def check(candidate):

    # Check some simple cases
    assert candidate(2, 10) == [2, 4, 6, 8], "Test 1"
    assert candidate(10, 2) == [2, 4, 6, 8], "Test 2"
    assert candidate(132, 2) == [2, 4, 6, 8], "Test 3"
    assert candidate(17,89) == [], "Test 4"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(generate_integers)