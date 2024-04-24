def max_sum_list(lists):
    max_sum = float('-inf')
    max_list = None

    for l in lists:
        current_sum = sum(l)
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = l

    return max_list

# Testing the function with examples




def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
    assert max_sum_list([[2,3,1]])==[2,3,1]

check(max_sum_list)