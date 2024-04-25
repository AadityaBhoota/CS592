def count_no_of_ways(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return k
    elif n == 2:
        return k * k
    
    same_color = k
    diff_color = k * (k - 1)
    
    for i in range(3, n + 1):
        new_same_color = diff_color
        new_diff_color = (same_color + diff_color) * (k - 1)
        
        same_color = new_same_color
        diff_color = new_diff_color
    
    total_ways = same_color + diff_color
    
    return total_ways

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)