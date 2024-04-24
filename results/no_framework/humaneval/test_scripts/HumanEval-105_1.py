def by_length(arr):
    if not arr:  # Check if the array is empty
        return []

    # Filter out strange numbers and keep only numbers between 1 and 9 inclusive
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # If there are no valid numbers in the array after filtering, return an empty array
    if not filtered_arr:
        return []

    # Sort the valid numbers, reverse the sorted array, and convert the numbers to their names
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    number_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [number_names[num - 1] for num in reversed_arr]

    return result

# Test Cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(arr1))  # Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

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