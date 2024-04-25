def square_perimeter(a):
    perimeter = 4 * a
    return perimeter

def check(candidate):
    assert square_perimeter(10)==40
    assert square_perimeter(5)==20
    assert square_perimeter(4)==16

check(square_perimeter)