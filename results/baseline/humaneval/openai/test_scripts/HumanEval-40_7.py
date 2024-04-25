def triples_sum_to_zero(l: list):
    if len(l) < 3:
        return False

    for i in range(len(l)-2):
        seen = set()
        for j in range(i+1, len(l)):
            if -(l[i] + l[j]) in seen:
                return True
            seen.add(l[j])

    return False



METADATA = {}


def check(candidate):
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([1, 3, 5, -1]) == False
    assert candidate([1, 3, -2, 1]) == True
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([1, 2, 5, 7]) == False
    assert candidate([2, 4, -5, 3, 9, 7]) == True
    assert candidate([1]) == False
    assert candidate([1, 3, 5, -100]) == False
    assert candidate([100, 3, 5, -100]) == False


check(triples_sum_to_zero)