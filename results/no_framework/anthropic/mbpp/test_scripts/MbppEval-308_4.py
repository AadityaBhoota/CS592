def large_product(nums1, nums2, N):
    """
    Find the specified number of largest products from two given lists, selecting one factor from each list.

    Args:
        nums1 (list): First list of numbers.
        nums2 (list): Second list of numbers.
        N (int): Number of largest products to return.

    Returns:
        list: List of the N largest products.
    """
    products = []
    for num1 in nums1:
        for num2 in nums2:
            product = num1 * num2
            products.append(product)

    # Sort the products in descending order and return the first N elements
    products.sort(reverse=True)
    return products[:N]

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)