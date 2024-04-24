def square_Sum(n):
    """
    Return the sum of squares of the first n odd natural numbers.
    
    Parameters:
    n (int): The number of odd natural numbers to consider.
    
    Returns:
    int: The sum of squares of the first n odd natural numbers.
    """
    sum_ = 0
    for i in range(1, 2*n+1, 2):
        sum_ += i**2
    return sum_

# Test the function with the given examples




def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)