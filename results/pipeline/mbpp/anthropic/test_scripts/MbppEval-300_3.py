def count_binary_seq(n):
    if n == 0:
        return 1.0
    
    total = 0
    for i in range(2 ** n):
        first_half = bin(i)[2:].zfill(n)
        second_half = bin((2 ** n) - 1 - i)[2:].zfill(n)
        if sum(int(bit) for bit in first_half) == sum(int(bit) for bit in second_half):
            total += 1
    return total

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)