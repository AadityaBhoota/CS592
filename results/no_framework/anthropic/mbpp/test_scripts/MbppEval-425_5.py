def count_element_in_list(list1, x):
    count = 0
    for sub_list in list1:
        if x in sub_list:
            count += 1
    return count

def check(candidate):
    assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1

check(count_element_in_list)