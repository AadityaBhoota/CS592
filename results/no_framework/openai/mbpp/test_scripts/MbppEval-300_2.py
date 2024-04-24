def count_binary_seq(n):
    # Check for the base case where n is 0 or 1
    if n == 0 or n == 1:
        return 2.0

    # Initialize the count of binary sequences
    count = 0

    for i in range(n+1):
        count += nCr(2*n, i)

    return count

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

# Test cases




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)