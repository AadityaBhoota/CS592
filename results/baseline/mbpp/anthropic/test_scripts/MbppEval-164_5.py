import math

def div_sum(n1, n2):
    """
    Determine if the sum of the divisors of two integers are the same.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        bool: True if the sum of the divisors of n1 and n2 are the same, False otherwise.
    """
    
    # Calculate the sum of divisors for n1
    sum_divisors_n1 = 1  # 1 is always a divisor
    for i in range(2, int(math.sqrt(n1)) + 1):
        if n1 % i == 0:
            sum_divisors_n1 += i
            if i != n1 // i:
                sum_divisors_n1 += n1 // i
    
    # Calculate the sum of divisors for n2
    sum_divisors_n2 = 1
    for i in range(2, int(math.sqrt(n2)) + 1):
        if n2 % i == 0:
            sum_divisors_n2 += i
            if i != n2 // i:
                sum_divisors_n2 += n2 // i
    
    # Compare the sums
    return sum_divisors_n1 == sum_divisors_n2

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)