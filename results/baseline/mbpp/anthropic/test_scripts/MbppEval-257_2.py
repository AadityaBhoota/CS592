def swap_numbers(a, b):
    """
    Write a function that takes in two numbers and returns a tuple with the second number and then the first number.

    Examples:
    swap_numbers(10,20) == (20,10)
    swap_numbers(15,17) == (17,15)
    swap_numbers(100,200) == (200,100)
    """
    return (b, a)

def check(candidate):
    assert swap_numbers(10,20)==(20,10)
    assert swap_numbers(15,17)==(17,15)
    assert swap_numbers(100,200)==(200,100)

check(swap_numbers)