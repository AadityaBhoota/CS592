def get_positive(l: list):
    positive_nums = []
    for num in l:
        if num > 0:
            positive_nums.append(num)
    return positive_nums



METADATA = {}


def check(candidate):
    assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]
    assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
    assert candidate([-1, -2]) == []
    assert candidate([]) == []


check(get_positive)