def max_product_tuple(list1):
    max_abs_product = None

    for tup in list1:
        product = abs(tup[0] * tup[1])
        if max_abs_product is None or product > max_abs_product:
            max_abs_product = product

    return max_abs_product

# Test the function with the provided examples




def check(candidate):
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
    assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484

check(max_product_tuple)