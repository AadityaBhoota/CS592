def median(l: list):
    sorted_lst = sorted(l)
    n = len(sorted_lst)

    if n % 2 == 0:
        mid_left = sorted_lst[n//2 - 1]
        mid_right = sorted_lst[n//2]
        return (mid_left + mid_right) / 2
    else:
        return sorted_lst[n//2]

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)