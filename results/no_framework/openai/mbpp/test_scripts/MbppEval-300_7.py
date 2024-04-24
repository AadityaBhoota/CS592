def count_binary_seq(n):
    def factorial(x):
        if x == 0:
            return 1
        return x * factorial(x - 1)

    def binomial_coefficient(n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))

    return binomial_coefficient(2 * n, n)

# Test cases




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)