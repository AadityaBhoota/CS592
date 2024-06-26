def tetrahedral_number(n):
    return (n * (n + 1) * (n + 2)) / 6

def check(candidate):
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84

check(tetrahedral_number)