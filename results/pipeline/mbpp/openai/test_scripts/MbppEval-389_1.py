def find_lucas(n): 
    '''
    Write a function to find the n'th lucas number.

    Examples:
    find_lucas(9) == 76
    find_lucas(4) == 7
    find_lucas(3) == 4
    '''
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer."
    
    lucas_numbers = [2, 1]  # Initialize with first two Lucas numbers
    
    for i in range(2, n+1):
        lucas_numbers.append(lucas_numbers[-1] + lucas_numbers[-2])  # Calculate the next Lucas number
        
    return lucas_numbers[n-1]  # Return the n-th Lucas number

def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)