def strange_sort_list(lst):
    sorted_list = []
    lst.sort()
    while lst:
        sorted_list.append(lst.pop(0))
        if lst:
            sorted_list.append(lst.pop())
    return sorted_list

# Test cases
print(strange_sort_list([1, 2, 3, 4]))  # should return [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # should return [5, 5, 5, 5]
print(strange_sort_list([]))  # should return []

def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
    assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
    assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert candidate([]) == []
    assert candidate([1,2,3,4,5,6,7,8]) == [1, 8, 2, 7, 3, 6, 4, 5]
    assert candidate([0,2,2,2,5,5,-5,-5]) == [-5, 5, -5, 5, 0, 2, 2, 2]
    assert candidate([111111]) == [111111]

    # Check some edge cases that are easy to work out by hand.
    assert True


check(strange_sort_list)