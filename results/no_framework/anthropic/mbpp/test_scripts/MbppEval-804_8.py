def is_product_even(arr):
    """
    Write a function to check whether the product of numbers in a list is even or not.

    Examples:
    is_product_even([1,2,3], 3) == True
    is_product_even([1,2,1,4], 4) == True
    is_product_even([1,1], 2) == False
    """
    product = 1
    for num in arr:
        product *= num
    return product % 2 == 0

def check(candidate):
    assert is_product_even([1,2,3])
    assert is_product_even([1,2,1,4])
    assert not is_product_even([1,1])

check(is_product_even)