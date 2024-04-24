def special_factorial(n):
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result *= factorial
        return result

# Test the function
n = 4


def check(candidate):

    # Check some simple cases
    assert candidate(4) == 288, "Test 4"
    assert candidate(5) == 34560, "Test 5"
    assert candidate(7) == 125411328000, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == 1, "Test 1"


check(special_factorial)