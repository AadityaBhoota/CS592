def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    Args:
        n (int): The index of the Fibonacci number to return.
    
    Returns:
        int: The n-th Fibonacci number.
    
    Raises:
        ValueError: If n is less than 1.
    
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    
    return b



METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


check(fib)