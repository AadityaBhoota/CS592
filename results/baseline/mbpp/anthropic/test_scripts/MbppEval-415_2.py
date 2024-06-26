def max_Product(arr):
    """
    Find a pair with the highest product from a given array of integers.

    Args:
        arr (list): The input array of integers.

    Returns:
        tuple: A tuple containing the pair of integers with the highest product.
    """
    if len(arr) < 2:
        return None

    # Initialize variables to keep track of the pair with the highest product
    max_pair = (arr[0], arr[1])
    max_product = max_pair[0] * max_pair[1]

    # Iterate through the array and update the max_pair if a pair with higher product is found
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_pair = (arr[i], arr[j])
                max_product = product

    return max_pair

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)