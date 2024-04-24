def sumofFactors(n):
    # Initialize the variable to store the sum of even factors
    sum_factors = 0

    # Iterate from 1 to square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        # Check if i is a factor of n and if it is even
        if n % i == 0 and i % 2 == 0:
            sum_factors += i
            # If the square root of n is not i, add the corresponding factor
            if n/i != i and n/i % 2 == 0:
                sum_factors += n//i

    return sum_factors

# Test cases




def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)