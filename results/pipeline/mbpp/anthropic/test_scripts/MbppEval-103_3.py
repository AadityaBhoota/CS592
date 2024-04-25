def eulerian_num(n, m):
    memo = {}
    
    def helper(n, m):
        if m == 0 or m == n:
            return 1
        if (n, m) in memo:
            return memo[(n, m)]
        memo[(n, m)] = (n - m) * helper(n - 1, m - 1) + (m + 1) * helper(n - 1, m)
        return memo[(n, m)]
    
    return helper(n, m)

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)