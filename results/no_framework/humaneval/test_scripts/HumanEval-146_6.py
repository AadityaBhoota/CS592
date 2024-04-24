def specialFilter(nums):
    def is_odd_digit(n):
        return int(str(abs(n))[0]) % 2 == 1 and int(str(abs(n))[-1]) % 2 == 1

    count = 0
    for num in nums:
        if num > 10 and is_odd_digit(num):
            count += 1

    return count

# Test cases
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2

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