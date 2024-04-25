def median(l: list):
    if not l:  # Check if the list is empty
        return None
    
    sorted_list = sorted(l)  # Sort the list
    
    n = len(sorted_list)
    if n % 2 != 0:  # If the length of the list is odd
        return sorted_list[n // 2]
    # If the length of the list is even
    return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)