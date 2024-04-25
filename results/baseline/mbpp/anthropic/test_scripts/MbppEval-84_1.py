def sequence(n):
    """
    Write a function to find the nth number in the newman conway sequence.

    Examples:
    sequence(10) == 6
    sequence(2) == 1
    sequence(3) == 2
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    prev1 = 1
    prev2 = 1
    curr = 2
    
    for i in range(3, n+1):
        curr = prev1 + sequence(prev2)
        prev1, prev2 = prev2, curr
    
    return curr

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)