def large_product(nums1, nums2, N):
    """
    Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.

    Examples:
    large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3) == [60, 54, 50]
    large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4) == [60, 54, 50, 48]
    large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5) == [60, 54, 50, 48, 45]
    """
    products = []
    for num1 in nums1:
        for num2 in nums2:
            products.append(num1 * num2)
    products.sort(reverse=True)
    return products[:N]

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)