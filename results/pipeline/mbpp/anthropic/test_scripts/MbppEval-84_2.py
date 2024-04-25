def sequence(n):
    """
    Find the nth number in the Newman-Conway sequence using dynamic programming.
    
    Args:
        n (int): The position of the number to be returned in the sequence.
        
    Returns:
        int: The nth number in the Newman-Conway sequence.
    """
    if n <= 2:
        return 1
    
    memo = {1: 1, 2: 1}
    
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)