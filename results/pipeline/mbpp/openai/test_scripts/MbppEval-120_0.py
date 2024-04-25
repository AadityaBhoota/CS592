def max_product_tuple(list1):
    max_product = float('-inf')  # Initialize max_product to negative infinity
    
    for tup in list1:  # Iterate through each tuple in the list
        product = abs(tup[0]) * abs(tup[1])  # Calculate the product of the absolute values of the numbers in the tuple
        max_product = max(max_product, product)  # Update max_product if the calculated product is larger
        
    return max_product  # Return the maximum product found

def check(candidate):
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
    assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484

check(max_product_tuple)