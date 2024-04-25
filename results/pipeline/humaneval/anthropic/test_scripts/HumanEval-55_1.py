def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to return.
    
    Returns:
        int: The nth Fibonacci number.
    
    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return b



METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


check(fib)