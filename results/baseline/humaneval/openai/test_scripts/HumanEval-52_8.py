def below_threshold(l: list, t: int) -> bool:
    for num in l:
        if num >= t:
            return False
    return True

# Test cases





METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10], 100)
    assert not candidate([1, 20, 4, 10], 5)
    assert candidate([1, 20, 4, 10], 21)
    assert candidate([1, 20, 4, 10], 22)
    assert candidate([1, 8, 4, 10], 11)
    assert not candidate([1, 8, 4, 10], 10)


check(below_threshold)