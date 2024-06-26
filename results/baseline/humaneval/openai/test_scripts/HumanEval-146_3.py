def specialFilter(nums):
    def is_odd_digit(num):
        return num % 2 != 0
    
    def first_last_odd(num):
        num_str = str(abs(num))
        return is_odd_digit(int(num_str[0])) and is_odd_digit(int(num_str[-1]))
    
    count = 0
    for num in nums:
        if num > 10 and first_last_odd(num):
            count += 1
    return count

# Test cases



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