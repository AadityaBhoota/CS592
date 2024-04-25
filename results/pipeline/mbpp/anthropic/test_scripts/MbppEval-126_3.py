def gcd(a, b):
    """Find the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def divisors(n):
    """Find all the divisors of n."""
    return [i for i in range(1, n + 1) if n % i == 0]

def sum(a, b):
    """Find the sum of common divisors of a and b."""
    g = gcd(a, b)
    return sum(divisors(g))

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)