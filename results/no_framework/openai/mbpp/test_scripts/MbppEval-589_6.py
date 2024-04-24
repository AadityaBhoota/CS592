def perfect_squares(a, b):
    result = []
    i = int(a**0.5) + 1
    while i**2 <= b:
        result.append(i**2)
        i += 1
    return result

# Test the function




def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)