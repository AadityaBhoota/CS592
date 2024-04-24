def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    
    same_color_count = k
    diff_color_count = k * (k - 1)
    
    for i in range(3, n + 1):
        total = (same_color_count + diff_color_count) * (k - 1)
        same_color_count = diff_color_count
        diff_color_count = total
    
    return same_color_count + diff_color_count

# Test cases




def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)