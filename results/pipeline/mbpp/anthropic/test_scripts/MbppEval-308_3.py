def large_product(nums1, nums2, N):
    largest_products = []
    for num1 in nums1:
        for num2 in nums2:
            product = num1 * num2
            if len(largest_products) < N or product > largest_products[0]:
                largest_products.append(product)
                largest_products.sort(reverse=True)
                if len(largest_products) > N:
                    largest_products.pop(0)
    return largest_products[:N]

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)