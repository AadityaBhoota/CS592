def bell_number(n):
    """
    Calculates the Bell number for the given input n.
    
    The Bell number B(n) represents the number of ways to partition a set of n elements.
    
    Args:
        n (int): The input value for which the Bell number is to be calculated.
        
    Returns:
        int: The Bell number for the given input n.
    """
    if n == 0:
        return 1
    
    bell = [0] * (n + 1)
    bell[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            bell[j] += bell[j - 1]
    
    return bell[n]

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)