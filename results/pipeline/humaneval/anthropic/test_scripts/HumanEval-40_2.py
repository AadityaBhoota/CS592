def triples_sum_to_zero(l: list):
    l.sort()
    found_triple = False
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        j = i + 1
        k = len(l) - 1
        while j < k:
            total = l[i] + l[j] + l[k]
            if total == 0:
                found_triple = True
                break
            elif total < 0:
                j += 1
            else:
                k -= 1
    return found_triple



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