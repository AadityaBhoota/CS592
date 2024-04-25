def tetrahedral_number(n):
    '''
    Write a function to find the nth tetrahedral number.

    Formula: Tn = n * (n + 1) * (n + 2) / 6
    '''
    
    result = (n * (n + 1) * (n + 2)) / 6
    return result

def check(candidate):
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84

check(tetrahedral_number)