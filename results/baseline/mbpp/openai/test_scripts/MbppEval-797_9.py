def sum_odd(n): 
    '''
    Write a python function to find the sum of all odd natural numbers within the range l and r.

    Examples:
    sum_in_Range(2,5) == 8
    sum_in_Range(5,7) == 12
    sum_in_Range(7,13) == 40
    '''
def sum_in_range(l, r):
    total = 0
    for num in range(l, r+1):
        if num % 2 != 0:  # Check if the number is odd
            total += num
    return total

# Test the function




def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)