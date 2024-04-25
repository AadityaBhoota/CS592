def max_subarray_product(arr):
    if not arr:
        return 0

    max_product_so_far = arr[0]
    current_max_product = arr[0]
    current_min_product = arr[0]

    for num in arr[1:]:
        temp_max = current_max_product
        current_max_product = max(num, num * current_max_product, num * current_min_product)
        current_min_product = min(num, num * temp_max, num * current_min_product)
        max_product_so_far = max(max_product_so_far, current_max_product)

    return max_product_so_far

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)