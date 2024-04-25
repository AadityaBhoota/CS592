def bell_Number(n):
    """
    Calculate the nth Bell number.

    The Bell number B(n) is the number of ways a set of n elements can be partitioned
    into non-empty subsets. It is calculated using the following recurrence relation:

    B(n) = sum(k=0 to n-1) of (binomial(n-1, k) * B(k))

    Args:
        n (int): The index of the Bell number to calculate.

    Returns:
        int: The nth Bell number.
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        bell = [0] * (n + 1)
        bell[0] = 1
        bell[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                bell[i] += binomial(i - 1, j) * bell[j]
        return bell[n]


def binomial(n, k):
    """
    Calculate the binomial coefficient C(n, k).

    Args:
        n (int): The total number of elements.
        k (int): The number of elements to choose.

    Returns:
        int: The binomial coefficient C(n, k).
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)