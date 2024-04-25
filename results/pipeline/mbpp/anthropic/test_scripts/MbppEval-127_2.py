def multiply_int(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return "Error: Both arguments must be integers."
    return x * y

def check(candidate):
    assert multiply_int(10,20)==200
    assert multiply_int(5,10)==50
    assert multiply_int(4,8)==32

check(multiply_int)