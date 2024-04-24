def amicable_numbers_sum(limit):
    """
    Finds the sum of all amicable numbers up to the given limit.
    
    An amicable pair is a set of two different numbers where each of the numbers is the sum of the proper divisors of the other number.
    
    Args:
        limit (int): The upper limit to search for amicable numbers.
        
    Returns:
        int: The sum of all amicable numbers up to the given limit.
    """
    # Create a dictionary to store the divisor sums for each number
    divisor_sums = {}
    
    # Calculate the divisor sums for all numbers up to the limit
    for i in range(1, limit):
        divisor_sums[i] = sum(divisor for divisor in range(1, i) if i % divisor == 0)
    
    # Find the amicable numbers and calculate their sum
    amicable_sum = 0
    for a in range(1, limit):
        b = divisor_sums[a]
        if b > a and a == divisor_sums[b]:
            amicable_sum += a + b
    
    return amicable_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)