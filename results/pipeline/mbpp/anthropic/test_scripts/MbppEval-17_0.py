def square_perimeter(a):
    perimeter = a * 4
    return perimeter

def check(candidate):
    assert square_perimeter(10)==40
    assert square_perimeter(5)==20
    assert square_perimeter(4)==16

check(square_perimeter)