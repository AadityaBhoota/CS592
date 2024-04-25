def min_product_tuple(list1):
    min_product = float('inf')
    
    for a, b in list1:
        product = a * b
        if product < min_product:
            min_product = product
    
    return min_product

def check(candidate):
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
    assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
    assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100

check(min_product_tuple)