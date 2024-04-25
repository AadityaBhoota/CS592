def sum_range_list(list1, m, n):
    if m < 0 or n >= len(list1) or m > n:
        return "Invalid range indices"
    
    sum_range = sum(list1[m:(n+1)])
    
    return sum_range

def check(candidate):
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38

check(sum_range_list)