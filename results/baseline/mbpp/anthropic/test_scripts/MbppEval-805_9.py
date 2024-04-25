def max_sum_list(lists):
    """
    Write a function that returns the list in a list of lists whose sum of elements is the highest.
    """
    if not lists:
        return []

    # Calculate the sum of each list
    sums = [sum(lst) for lst in lists]

    # Find the index of the list with the maximum sum
    max_index = sums.index(max(sums))

    # Return the list with the maximum sum
    return lists[max_index]

def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
    assert max_sum_list([[2,3,1]])==[2,3,1]

check(max_sum_list)