def generate_integers(a, b):
    even_digits = []

    # Make sure a is less than or equal to b
    if a > b:
        a, b = b, a

    # Iterate through the range and append even digits to the list
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)

    # Sort the list in ascending order
    even_digits.sort()

    return even_digits

def check(candidate):

    # Check some simple cases
    assert candidate(2, 10) == [2, 4, 6, 8], "Test 1"
    assert candidate(10, 2) == [2, 4, 6, 8], "Test 2"
    assert candidate(132, 2) == [2, 4, 6, 8], "Test 3"
    assert candidate(17,89) == [], "Test 4"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(generate_integers)