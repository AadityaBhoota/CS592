def issort_list(list1):
    '''
    Write a function to check whether a specified list is sorted or not.

    Examples:
    issort_list([1,2,4,6,8,10,12,14,16,17]) == True
    issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17]) == False
    issort_list([1, 2, 4, 6, 8, 10,15,14,20]) == False
    '''
def is_sorted(lst):
    """
    Check whether a specified list is sorted or not.

    Examples:
    is_sorted([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]) == True
    is_sorted([1, 2, 4, 6, 8, 10, 12, 14, 20, 17]) == False
    is_sorted([1, 2, 4, 6, 8, 10, 15, 14, 20]) == False
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def check(candidate):
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False

check(issort_list)