def by_length(arr):
    name_mapping = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    # Filter out strange numbers and sort the remaining numbers
    filtered_arr = sorted([num for num in arr if 1 <= num <= 9])

    # Replace the numbers with their corresponding names
    names_arr = [name_mapping[num] for num in reversed(filtered_arr)]

    return names_arr

# Test cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
arr2 = []
arr3 = [1, -1, 55]





def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([1, -1 , 55]) == ['One'], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, -1, 3, 2]) == ["Three", "Two", "One"]
    assert candidate([9, 4, 8]) == ["Nine", "Eight", "Four"]


check(by_length)