def square_Sum(n):  
    total = 0
    
    for i in range(1, 2*n+1):
        if i % 2 == 0:
            total += i**2

    return total

# Test cases




def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)