def _recursive_list_sum(data):
    total = 0
    for element in data:
        if isinstance(element, list):
            total += _recursive_list_sum(element)
        else:
            total += element
    return total

def recursive_list_sum(data_list):
    return _recursive_list_sum(data_list)

def check(candidate):
    assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
    assert recursive_list_sum(([7, 10, [15,14],[19,41]]))==106
    assert recursive_list_sum(([10, 20, [30,40],[50,60]]))==210

check(recursive_list_sum)