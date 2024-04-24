def by_length(arr):
    mapping = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

    # Filter out numbers that are between 1 and 9 inclusive
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # Sort the filtered array, reverse it, and map the numbers to their corresponding names
    result = [mapping[num] for num in sorted(filtered_arr, reverse=True)]

    return result

# Test cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(arr1))  # Output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

arr2 = []
print(by_length(arr2))  # Output: []

arr3 = [1, -1, 55]
print(by_length(arr3))  # Output: ['One']

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