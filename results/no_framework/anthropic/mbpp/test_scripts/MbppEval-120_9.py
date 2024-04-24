def max_product_tuple(list1):
    """
    Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.

    Examples:
    max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
    max_product_tuple([(10, 20), (15, 2), (5, 10)]) == 200
    max_product_tuple([(11, 44), (10, 15), (20, 5), (12, 9)]) == 484
    """
    max_product = 0
    for a, b in list1:
        product = abs(a * b)
        if product > max_product:
            max_product = product
    return max_product

def check(candidate):
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
    assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484

check(max_product_tuple)