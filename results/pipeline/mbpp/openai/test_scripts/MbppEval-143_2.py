def find_lists(Input):
    count = 0  # Step 2: Initialize a variable to count the number of lists in the tuple

    for element in Input:
        if isinstance(element, list):  # Step 4: Check if the current element is a list
            count += 1

    return count  # Step 5: Return the count of lists in the tuple

def check(candidate):
    assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
    assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1

check(find_lists)