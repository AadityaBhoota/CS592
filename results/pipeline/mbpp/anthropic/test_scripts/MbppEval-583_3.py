from math import factorial

def catalan_number(n):
    """
    Returns the nth Catalan number.
    
    Args:
        n (int): The index of the Catalan number to be calculated.
        
    Returns:
        int: The nth Catalan number.
    """
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)