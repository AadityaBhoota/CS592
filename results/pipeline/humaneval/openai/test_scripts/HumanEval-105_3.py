def by_length(arr):
    # Define a dictionary to map integers to their corresponding names
    integer_to_name = {
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
    
    # Filter out integers between 1 and 9 (inclusive) from the input array and sort these integers
    filtered_arr = sorted([num for num in arr if 1 <= num <= 9])
    
    # Reverse the sorted array of integers
    reversed_arr = filtered_arr[::-1]
    
    # Map each integer in the reversed array to its corresponding name using the dictionary
    result_arr = [integer_to_name[num] for num in reversed_arr]
    
    return result_arr

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