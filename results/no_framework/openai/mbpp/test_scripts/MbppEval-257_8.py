def swap_numbers(a, b):
    return (b, a)

# Test the function




def check(candidate):
    assert swap_numbers(10,20)==(20,10)
    assert swap_numbers(15,17)==(17,15)
    assert swap_numbers(100,200)==(200,100)

check(swap_numbers)