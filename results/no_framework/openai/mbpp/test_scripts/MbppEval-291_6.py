def count_no_of_ways(n, k):
    if n == 0:
        return 0
    
    same_color, diff_color = 0, k

    for i in range(2, n+1):
        same_color, diff_color = diff_color, (same_color + diff_color) * (k-1)

    return same_color + diff_color

# Test the function with the given examples




def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)