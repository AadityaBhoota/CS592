def median(l: list):
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 1:  # Odd number of elements
        return sorted_list[n // 2]
    else:  # Even number of elements
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

# Test the function with the provided examples





METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)