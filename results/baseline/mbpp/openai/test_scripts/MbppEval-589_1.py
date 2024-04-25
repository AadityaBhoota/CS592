import math

def perfect_squares(a, b):
    squares = []
    for i in range(int(math.sqrt(a)), int(math.sqrt(b))+1):
        if i*i >= a and i*i <= b:
            squares.append(i*i)
    return squares

# Test cases




def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)