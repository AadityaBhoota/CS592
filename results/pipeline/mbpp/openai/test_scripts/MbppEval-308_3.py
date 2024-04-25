def large_product(nums1, nums2, N):
    # Input validation
    if len(nums1) != len(nums2):
        return "Error: Input lists should be of the same length."
    if N <= 0 or N > len(nums1):
        return "Error: Specified number N should be within the range [1, length of the lists]."

    # Generate products
    products = [nums1[i] * nums2[i] for i in range(len(nums1))]

    # Sort products in descending order
    sorted_products = sorted(products, reverse=True)

    return sorted_products[:N]

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)