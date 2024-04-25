def max_element(l: list):
    max_val = l[0]
    for x in l:
        if x > max_val:
            max_val = x
    return max_val



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

check(max_element)