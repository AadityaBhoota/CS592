def issort_list(list1):
    is_sorted = True
    for i in range(1, len(list1)):
        if list1[i] < list1[i-1]:
            is_sorted = False
            break
    return is_sorted

def check(candidate):
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False

check(issort_list)