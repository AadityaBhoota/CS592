def count_no_of_ways(n, k): 
    total_ways = k * k
    dp_same = k
    dp_diff = k
    
    for i in range(3, n+1):
        new_dp_same = dp_diff
        new_dp_diff = (dp_same + dp_diff) * (k-1)
        dp_same = new_dp_same
        dp_diff = new_dp_diff
        
    return dp_same + dp_diff

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)