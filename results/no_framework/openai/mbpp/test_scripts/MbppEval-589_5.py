def perfect_squares(a, b):
    squares = [x**2 for x in range(int(a ** 0.5), int(b ** 0.5) + 1) if x**2 >= a and x**2 <= b]
    return squares

# Test cases




def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)