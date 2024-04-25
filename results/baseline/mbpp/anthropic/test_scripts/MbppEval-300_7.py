def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that the sum of the first n bits is the same as the sum of the last n bits.

    Examples:
    count_binary_seq(1) == 2.0
    count_binary_seq(2) == 6.0
    count_binary_seq(3) == 20.0
    """
    if n == 0:
        return 1.0
    
    total = 0
    for i in range(2 ** n):
        first_half = bin(i)[2:].zfill(n)
        second_half = bin(i)[2:].zfill(n)[::-1]
        if sum(map(int, first_half)) == sum(map(int, second_half)):
            total += 1
    
    return total

# Test cases




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)