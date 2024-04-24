def hexagonal_num(n):
    return n * (2 * n - 1)

# Test the function with the provided examples




def check(candidate):
    assert hexagonal_num(10) == 190
    assert hexagonal_num(5) == 45
    assert hexagonal_num(7) == 91

check(hexagonal_num)