def issort_list(list1):
    return all(list1[i] <= list1[i+1] for i in range(len(list1) - 1))

# Test cases




def check(candidate):
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False

check(issort_list)