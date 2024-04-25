def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    
    product = 1  # Initialize the product to 1
    digits_list = [int(d) for d in str(n)]  # Extract individual digits from the given number
    odd_digits = [d for d in digits_list if d % 2 != 0]  # Check if each digit is odd
    
    for digit in odd_digits:
        product *= digit  # Multiply each odd digit with the running product
    
    return product  # Return the final product

def check(candidate):

    # Check some simple cases
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625

    # Check some edge cases that are easy to work out by hand.
    assert candidate(2468) == 0


check(digits)