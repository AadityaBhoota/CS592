def eulerian_num(n, m):
    if n == 0 and m == 0:
        return 1
    
    if n == 1 and m == 0:
        return 0
    
    if m > n:
        return 0
    
    return (n-m) * eulerian_num(n-1, m-1) + (m+1) * eulerian_num(n-1, m)

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)