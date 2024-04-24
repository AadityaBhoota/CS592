def square_Sum(n):  
    sum_result = 0
    for i in range(1, 2*n, 2):  # iterate through the first n odd natural numbers
        sum_result += i**2  # calculate the square of each number and add it to the sum
    return sum_result

# Test cases




def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)