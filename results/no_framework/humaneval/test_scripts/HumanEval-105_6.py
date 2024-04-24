def by_length(arr):
    if not arr:
        return []

    # Filter out strange numbers and select only integers between 1 and 9
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    if not filtered_arr:
        return []

    sorted_arr = sorted(filtered_arr)
    reversed_arr = list(reversed(sorted_arr))

    num_to_name = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    return [num_to_name[num] for num in reversed_arr]

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # Output: []
print(by_length([1, -1 , 55]))  # Output: ['One']

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