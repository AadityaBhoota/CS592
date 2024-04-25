import math

def perfect_squares(a, b):
    perfect_squares_list = []
    for num in range(a, b + 1):
        if int(math.sqrt(num)) ** 2 == num:
            perfect_squares_list.append(num)
    return perfect_squares_list

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)