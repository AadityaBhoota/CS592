def get_max_sum(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    max_sum = max(n, get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5))
    
    memo[n] = max_sum
    return max_sum

# Examples




def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )