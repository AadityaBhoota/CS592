def median(l: list):
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        return (sorted_list[mid1] + sorted_list[mid2]) / 2
    else:
        mid = n // 2
        return sorted_list[mid]



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)