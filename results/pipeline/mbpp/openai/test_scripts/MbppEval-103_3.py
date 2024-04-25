def eulerian_num(n, m):
    def eulerian_recursive(n, m):
        if m > n:
            return 0
        if m == 0:
            return 1 if n == 0 else 0
        
        return (n - m) * eulerian_recursive(n - 1, m) + (m + 1) * eulerian_recursive(n - 1, m - 1)
    
    return eulerian_recursive(n, m)

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)