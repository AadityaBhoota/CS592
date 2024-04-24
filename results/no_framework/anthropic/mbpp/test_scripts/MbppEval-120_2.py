def max_product_tuple(list1):
    """
    Find the maximum absolute product between numbers in pairs of tuples within a given list.

    Args:
        list1 (list): A list of tuples, where each tuple contains two integers.

    Returns:
        int: The maximum absolute product between numbers in pairs of tuples.
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