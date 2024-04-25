def unique_product(list_data):
    unique_set = set()
    
    # Step 1: Iterate through the list and add unique elements to the set
    for num in list_data:
        unique_set.add(num)

    # Step 2: Calculate the product of unique elements
    unique_product = 1
    for num in unique_set:
        unique_product *= num

    return unique_product

def check(candidate):
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert unique_product([1, 2, 3, 1,]) == 6
    assert unique_product([7, 8, 9, 0, 1, 1]) == 0

check(unique_product)