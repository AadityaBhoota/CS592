def sum_to_n(n: int) -> int:
    """
    Sums the numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the range.
        
    Returns:
        int: The sum of the numbers from 1 to n.
    """
    return n * (n + 1) // 2



METADATA = {}


def check(candidate):
    assert candidate(1) == 1
    assert candidate(6) == 21
    assert candidate(11) == 66
    assert candidate(30) == 465
    assert candidate(100) == 5050


check(sum_to_n)