def bell_Number(n):
    """
    Calculates the nth Bell number.

    The Bell number B(n) is the number of ways a set of n distinct objects
    can be partitioned into non-empty subsets.

    Args:
        n (int): The index of the Bell number to calculate.

    Returns:
        int: The nth Bell number.
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
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)