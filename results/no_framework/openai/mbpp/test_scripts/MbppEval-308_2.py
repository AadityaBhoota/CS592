def large_product(nums1, nums2, N):
    products = []
    for n1 in nums1:
        for n2 in nums2:
            products.append(n1 * n2)

    largest_products = sorted(products, reverse=True)[:N]

    return largest_products

# Test cases




def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)