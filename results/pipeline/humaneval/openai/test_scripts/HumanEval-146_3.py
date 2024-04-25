def specialFilter(nums):
    count = 0  # Initialize a counter variable to keep track of the number of elements that meet the specified conditions
    
    for num in nums:
        # Check if the number is greater than 10 and if both the first and last digits are odd
        str_num = str(abs(num))  # Convert the number to a string and take the absolute value to handle negative numbers
        first_digit = int(str_num[0])  # Get the first digit of the number
        last_digit = abs(num) % 10  # Get the last digit of the number

        # If the number meets the conditions, increment the counter
        if num > 10 and first_digit % 2 != 0 and last_digit % 2 != 0:
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