def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 1:
        return sorted_lst[n//2]
    else:
        middle_1 = sorted_lst[n//2 - 1]
        middle_2 = sorted_lst[n//2]
        return (middle_1 + middle_2) / 2

# Test cases





METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)