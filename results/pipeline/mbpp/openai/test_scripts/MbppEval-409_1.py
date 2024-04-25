def min_product_tuple(list1):
    min_product = float('inf')  # Step 2

    for tup in list1:  # Step 3
        product = tup[0] * tup[1]  # Step 4
        if product < min_product:  # Step 5
            min_product = product

    return min_product  # Step 6

def check(candidate):
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
    assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
    assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100

check(min_product_tuple)