def max_sum_list(lists):
    """
    Write a function that returns the list in a list of lists whose sum of elements is the highest.

    Examples:
    max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [10, 11, 12]
    max_sum_list([[3,2,1], [6,5,4], [12,11,10]]) == [12,11,10]
    max_sum_list([[2,3,1]]) == [2,3,1]
    """
    if not lists:
        return []
    
    max_sum = 0
    max_list = None
    
    for lst in lists:
        current_sum = sum(lst)
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = lst
    
    return max_list

def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
    assert max_sum_list([[2,3,1]])==[2,3,1]

check(max_sum_list)