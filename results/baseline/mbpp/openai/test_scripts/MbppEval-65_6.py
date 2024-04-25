def recursive_list_sum(data_list):
    total_sum = 0
    
    for element in data_list:
        if isinstance(element, list):
            total_sum += recursive_list_sum(element)
        else:
            total_sum += element

    return total_sum

# Test cases




def check(candidate):
    assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
    assert recursive_list_sum(([7, 10, [15,14],[19,41]]))==106
    assert recursive_list_sum(([10, 20, [30,40],[50,60]]))==210

check(recursive_list_sum)