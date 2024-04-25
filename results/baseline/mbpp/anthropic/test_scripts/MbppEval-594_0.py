def diff_even_odd(list1):
    """
    Write a function to find the difference of the first even and first odd number of a given list.

    Examples:
    diff_even_odd([1,3,5,7,4,1,6,8]) == 3
    diff_even_odd([1,2,3,4,5,6,7,8,9,10]) == 1
    diff_even_odd([1,5,7,9,10]) == 9
    """
    # Initialize variables to keep track of the first even and odd numbers
    first_even = None
    first_odd = None

    # Iterate through the list
    for num in list1:
        # Check if the number is even
        if num % 2 == 0 and first_even is None:
            first_even = num
        # Check if the number is odd
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        # If we have found both the first even and odd numbers, we can exit the loop
        if first_even is not None and first_odd is not None:
            break

    # If either the first even or odd number was not found, return None
    if first_even is None or first_odd is None:
        return None

    # Return the difference between the first even and odd numbers
    return abs(first_even - first_odd)

def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)