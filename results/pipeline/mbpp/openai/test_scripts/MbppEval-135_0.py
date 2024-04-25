def hexagonal_num(n):
    if not isinstance(n, int) or n <= 0:
        return None
    
    hexagonal_number = n * (2*n - 1)
    return hexagonal_number

def check(candidate):
    assert hexagonal_num(10) == 190
    assert hexagonal_num(5) == 45
    assert hexagonal_num(7) == 91

check(hexagonal_num)