def multiply_int(x, y):
    return x * y

# Test the function with the given examples




def check(candidate):
    assert multiply_int(10,20)==200
    assert multiply_int(5,10)==50
    assert multiply_int(4,8)==32

check(multiply_int)