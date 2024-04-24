def odd_num_sum(n):
    '''
    This function calculates the sum of the fourth powers of the first n odd natural numbers.

    Parameters:
    n (int): The number of odd natural numbers to consider.

    Returns:
    int: The sum of the fourth powers of the first n odd natural numbers.
    '''
    sum = 0
    for i in range(1, 2*n+1, 2):
        sum += i**4
    return sum

# Test the function




def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)