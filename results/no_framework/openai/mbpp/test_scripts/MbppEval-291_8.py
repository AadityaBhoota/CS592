def count_no_of_ways(n, k):
    if n == 0:
        return 0
    
    same_color = [0] * n
    diff_color = [0] * n

    same_color[0] = diff_color[0] = k

    for i in range(1, n):
        same_color[i] = diff_color[i-1]
        diff_color[i] = (same_color[i-1] + diff_color[i-1]) * (k-1)

    return same_color[-1] + diff_color[-1]

# Test cases




def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)