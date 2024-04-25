def max_sum_list(lists):
    max_sum = 0
    max_list = None
    
    for l in lists:
        curr_sum = sum(l)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_list = l
    
    return max_list

def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
    assert max_sum_list([[2,3,1]])==[2,3,1]

check(max_sum_list)