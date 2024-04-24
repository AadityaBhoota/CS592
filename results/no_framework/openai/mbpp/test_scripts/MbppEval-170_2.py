def sum_range_list(list1, m, n):
    if m > n:
        m, n = n, m
    
    total = 0
    for num in list1:
        if m <= list1.index(num) <= n:
            total += num
    
    return total

# Test cases




def check(candidate):
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38

check(sum_range_list)