def eulerian_num(n, m): 
    if n == 0:
        return 1
    elif m == 0:
        return 0
    elif m == 1:
        return n + 1
    
    def eulerian_helper(i, j, memo):
        if i == 0:
            return 1
        elif j == 0:
            return 0
        elif memo[i][j] != -1:
            return memo[i][j]
        
        result = (j + 1) * eulerian_helper(i - 1, j, memo) + (i - j) * eulerian_helper(i - 1, j - 1, memo)
        memo[i][j] = result
        return result
    
    memo = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    
    return eulerian_helper(n, m, memo)

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)