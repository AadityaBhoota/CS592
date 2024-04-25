def get_positive(l: list):
    pos_nums = []
    
    # Iterate through the input list.
    for num in l:
        # Check if the number is positive.
        if num > 0:
            # If it is positive, add it to the new list.
            pos_nums.append(num)
    
    return pos_nums



METADATA = {}


def check(candidate):
    assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]
    assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
    assert candidate([-1, -2]) == []
    assert candidate([]) == []


check(get_positive)