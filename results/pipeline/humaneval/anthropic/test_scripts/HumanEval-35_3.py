def max_element(l: list):
    if not l:
        return None
    max_val = l[0]
    for num in l[1:]:
        if num > max_val:
            max_val = num
    return max_val



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

check(max_element)