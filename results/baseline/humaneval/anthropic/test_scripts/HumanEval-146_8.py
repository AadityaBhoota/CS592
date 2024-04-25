def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns
    the number of elements in the array that are greater than 10 and both
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    """
    count = 0
    for num in nums:
        # Ignore negative numbers
        if num < 0:
            continue
        # Convert the number to a string and check the first and last digits
        first_digit = int(str(num)[0])
        last_digit = int(str(num)[-1])
        if num > 10 and first_digit % 2 == 1 and last_digit % 2 == 1:
            count += 1
    return count

def check(candidate):

    # Check some simple cases
    assert candidate([5, -2, 1, -5]) == 0  
    assert candidate([15, -73, 14, -15]) == 1
    assert candidate([33, -2, -3, 45, 21, 109]) == 2
    assert candidate([43, -12, 93, 125, 121, 109]) == 4
    assert candidate([71, -2, -33, 75, 21, 19]) == 3


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1]) == 0              
    assert candidate([]) == 0                   


check(specialFilter)