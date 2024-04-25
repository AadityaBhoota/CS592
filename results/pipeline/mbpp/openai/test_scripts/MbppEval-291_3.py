def count_no_of_ways(n, k): 
    '''
    Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.

    Examples:
    count_no_of_ways(2, 4) == 16
    count_no_of_ways(3, 2) == 6
    count_no_of_ways(4, 4) == 228
    '''
    
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k
    
    same_color = k
    diff_color = k
    
    for i in range(3, n+1):
        prev_same_color = same_color
        same_color = diff_color
        diff_color = (prev_same_color + diff_color) * (k - 1)
    
    return same_color + diff_color

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)