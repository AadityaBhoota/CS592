def max_Product(arr):
    # Initialize variables to keep track of the smallest and second smallest values
    smallest = float('inf')
    second_smallest = float('inf')
    
    # Initialize variables to keep track of the largest and second largest values
    largest = float('-inf')
    second_largest = float('-inf')
    
    # Iterate through the array
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
            
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
            
    # Check if the product of smallest and second smallest is greater than the product of largest and second largest
    if smallest * second_smallest > largest * second_largest:
        return (smallest, second_smallest)
    else:
        return (largest, second_largest)

# Test examples




def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)