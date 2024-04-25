def max_element(l: list):
    max_val = l[0]
    
    for val in l[1:]:
        if val > max_val:
            max_val = val
    
    return max_val



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

check(max_element)