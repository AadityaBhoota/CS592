def max_sum_list(lists):
    max_list = []
    max_sum = float('-inf')
    
    for lst in lists:
        if sum(lst) > max_sum:
            max_sum = sum(lst)
            max_list = lst
    
    return max_list

# Test the function




def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
    assert max_sum_list([[2,3,1]])==[2,3,1]

check(max_sum_list)