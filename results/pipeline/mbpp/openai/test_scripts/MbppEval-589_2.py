import math

def perfect_squares(a, b):
    squares_list = []
    
    for i in range(a, b+1):
        if math.isqrt(i) ** 2 == i:
            squares_list.append(i)
    
    return squares_list

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)