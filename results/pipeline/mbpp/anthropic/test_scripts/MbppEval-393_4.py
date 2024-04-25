def max_length_list(input_list):
    max_length = 0
    max_list = None
    
    for lst in input_list:
        if len(lst) > max_length:
            max_length = len(lst)
            max_list = lst
    
    return (max_length, max_list)

def check(candidate):
    assert max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length_list([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(5,[1,2,3,4,5])
    assert max_length_list([[3,4,5],[6,7,8,9],[10,11,12]])==(4,[6,7,8,9])

check(max_length_list)