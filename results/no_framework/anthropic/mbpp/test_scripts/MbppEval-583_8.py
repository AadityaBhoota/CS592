def catalan_number(n):
    """
    Calculates the nth Catalan number.

    Args:
        n (int): The index of the Catalan number to be calculated.

    Returns:
        int: The nth Catalan number.
    """
    if n == 0:
        return 1
    
    catalan_numbers = [0] * (n + 1)
    catalan_numbers[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            catalan_numbers[i] += catalan_numbers[j] * catalan_numbers[i - j - 1]
    
    return catalan_numbers[n]

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)