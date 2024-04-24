def max_Product(arr):
    """
    Find a pair with highest product from a given array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the pair with the highest product.
    """
    # Sort the array in descending order
    arr.sort(reverse=True)

    # Check the product of the first two elements
    max_product = arr[0] * arr[1]

    # Check the product of the last two negative elements (if any)
    if len(arr) >= 2 and arr[-1] < 0 and arr[-2] < 0:
        negative_product = arr[-1] * arr[-2]
        max_product = max(max_product, negative_product)

    return (arr[0], arr[1])

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)