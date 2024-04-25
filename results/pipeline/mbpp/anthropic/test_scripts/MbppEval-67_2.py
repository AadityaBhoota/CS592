def bell_number(n):
    """
    Write a function to find the number of ways to partition a set of Bell numbers.

    Examples:
    bell_number(2) == 2
    bell_number(10) == 115975
    bell_number(56) == 6775685320645824322581483068371419745979053216268760300
    """
    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        result = sum(helper(k) * binomial(n, k) for k in range(n))
        memo[n] = result
        return result

    return helper(n)

def binomial(n, k):
    """
    Calculate the binomial coefficient C(n, k).
    """
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    """
    Calculate the factorial of a number.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)