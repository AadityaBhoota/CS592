def bell_number(n):
    """
    Computes the Bell number B(n).
    """
    if n == 0 or n == 1:
        return 1
    
    result = 0
    for k in range(n):
        result += bell_number(k) * binomial(n, k)
    
    return result

def binomial(n, k):
    """
    Computes the binomial coefficient C(n, k).
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    """
    Computes the factorial of a number.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)