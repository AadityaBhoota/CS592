def median(l: list):
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 0:
        # If the number of elements is even, take the average of the middle two elements
        mid_left = n // 2 - 1
        mid_right = n // 2
        return (sorted_list[mid_left] + sorted_list[mid_right]) / 2
    else:
        # If the number of elements is odd, return the middle element
        mid_index = n // 2
        return sorted_list[mid_index]

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