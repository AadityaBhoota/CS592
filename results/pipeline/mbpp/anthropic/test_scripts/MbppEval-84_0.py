def sequence(n):
    """
    Find the nth number in the Newman-Conway sequence.

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The nth number in the Newman-Conway sequence.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    return 1 + sum(1 for k in range(1, n) if n % k == 0)

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)