def is_polite(n):
    """
    Find the nth polite number.
    
    The nth polite number is defined as the smallest positive integer k such that
    the sum of the divisors of k (including k) is exactly n.
    
    Args:
        n (int): The index of the polite number to find.
        
    Returns:
        int: The nth polite number.
    """
    k = n
    while True:
        if sum(divisors(k)) == n:
            return k
        k += 1

def divisors(n):
    """
    Find all the divisors of a number.
    
    Args:
        n (int): The number to find the divisors of.
        
    Returns:
        list: The list of divisors of n.
    """
    divisors_list = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n // i:
                divisors_list.append(n // i)
    divisors_list.append(n)
    return divisors_list

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)