def is_product_even(arr):
    product = 1
    for num in arr:
        product *= num

    return product % 2 == 0

# Test cases




def check(candidate):
    assert is_product_even([1,2,3])
    assert is_product_even([1,2,1,4])
    assert not is_product_even([1,1])

check(is_product_even)