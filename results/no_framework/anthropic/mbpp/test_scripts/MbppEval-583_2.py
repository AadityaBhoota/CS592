def catalan_number(n):
    """
    Returns the nth Catalan number.

    The Catalan numbers are a sequence of natural numbers that occur in various counting problems, often involving recursively-defined objects. The first few Catalan numbers are:
    0, 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, ...

    Args:
        n (int): The index of the Catalan number to calculate.

    Returns:
        int: The nth Catalan number.
    """
    if n == 0:
        return 1
    
    result = 0
    for i in range(n):
        result += catalan_number(i) * catalan_number(n - i - 1)
    
    return result

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)