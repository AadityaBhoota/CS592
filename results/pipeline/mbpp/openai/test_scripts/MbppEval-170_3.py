def sum_range_list(list1, m, n):
    if m < 0 or n > len(list1):
        return "Indices are out of range"

    sublist = list1[m:n + 1]
    sublist_sum = sum(sublist)

    return sublist_sum

def check(candidate):
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38

check(sum_range_list)