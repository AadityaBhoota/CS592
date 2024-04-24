def sequence(n):
    """
    Write a function to find the nth number in the Newman-Conway sequence.

    Examples:
    sequence(10) == 6
    sequence(2) == 1
    sequence(3) == 2
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    # Initialize the first two terms
    a = 1
    b = 1
    
    # Compute the remaining terms
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    
    return b

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)