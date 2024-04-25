def multiply_int(x, y):
    """
    Write a function to multiply two integers.

    Examples:
    multiply_int(10,20) == 200
    multiply_int(5,10) == 50
    multiply_int(4,8) == 32
    """
    return x * y

def check(candidate):
    assert multiply_int(10,20)==200
    assert multiply_int(5,10)==50
    assert multiply_int(4,8)==32

check(multiply_int)