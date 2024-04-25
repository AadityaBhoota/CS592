def find(n, m):
    """
    Write a Python function to find the quotient of two numbers (rounded down to the nearest integer).

    Examples:
    find(10, 3) == 3
    find(4, 2) == 2
    find(20, 5) == 4
    """
    return n // m

def check(candidate):
    assert find(10,3) == 3
    assert find(4,2) == 2
    assert find(20,5) == 4

check(find)