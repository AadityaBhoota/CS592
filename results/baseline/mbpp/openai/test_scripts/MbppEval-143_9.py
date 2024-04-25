def find_lists(Input):
    count = 0
    for item in Input:
        if isinstance(item, list):
            count += 1
    return count

# Testing the function with the provided examples




def check(candidate):
    assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
    assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1

check(find_lists)