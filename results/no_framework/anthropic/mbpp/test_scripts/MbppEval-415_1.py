def max_product(arr):
    """
    Find a pair with the highest product from a given array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the two integers that have the highest product.
    """
    if len(arr) < 2:
        return None

    # Initialize the maximum product and the pair with the highest product
    max_prod = float('-inf')
    max_pair = None

    # Iterate through the array and find the pair with the highest product
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_prod:
                max_prod = product
                max_pair = (arr[i], arr[j])

    return max_pair

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)