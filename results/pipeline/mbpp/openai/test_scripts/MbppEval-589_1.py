import math

def perfect_squares(a, b):
    perfect_squares_list = []
    smallest_square = math.ceil(math.sqrt(a))
    largest_square = math.floor(math.sqrt(b))

    for i in range(smallest_square, largest_square + 1):
        square = i * i
        if a <= square <= b:
            perfect_squares_list.append(square)

    return perfect_squares_list

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)