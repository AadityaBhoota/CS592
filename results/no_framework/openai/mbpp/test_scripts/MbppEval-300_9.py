def count_binary_seq(n): 
    # Function to calculate factorial
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    # Formula to calculate count of binary sequences
    count = factorial(2*n) / (factorial(n) * factorial(n) * (n + 1))
    return count

# Test cases




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)