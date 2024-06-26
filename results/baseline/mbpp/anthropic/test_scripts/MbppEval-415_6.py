def max_Product(arr):
    """
    Find a pair with the highest product from a given array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the pair of integers with the highest product.
    """
    if len(arr) < 2:
        return None

    # Initialize the maximum product and the pair of integers
    max_prod = arr[0] * arr[1]
    max_pair = (arr[0], arr[1])

    # Iterate through the array to find the pair with the highest product
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            prod = arr[i] * arr[j]
            if prod > max_prod:
                max_prod = prod
                max_pair = (arr[i], arr[j])

    return max_pair

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)