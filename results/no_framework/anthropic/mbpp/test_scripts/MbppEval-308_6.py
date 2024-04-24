def large_product(nums1, nums2, N):
    """
    Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.

    Examples:
    large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3) == [60, 54, 50]
    large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4) == [60, 54, 50, 48]
    large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5) == [60, 54, 50, 48, 45]
    """
    # Sort both lists in descending order
    nums1.sort(reverse=True)
    nums2.sort(reverse=True)

    # Initialize an empty list to store the largest products
    largest_products = []

    # Iterate through the first N elements of each list and multiply them
    for i in range(N):
        product = nums1[i] * nums2[i]
        largest_products.append(product)

    # Sort the list of products in descending order and return the first N elements
    largest_products.sort(reverse=True)
    return largest_products[:N]

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)