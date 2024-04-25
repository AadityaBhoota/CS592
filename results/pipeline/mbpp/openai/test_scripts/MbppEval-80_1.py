def tetrahedral_number(n):
    tetrahedral_num = n * (n + 1) * (n + 2) / 6
    return float(tetrahedral_num)

def check(candidate):
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84

check(tetrahedral_number)