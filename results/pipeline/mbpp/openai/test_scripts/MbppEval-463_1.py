def max_subarray_product(arr):
    max_product = arr[0]
    min_product = arr[0]
    result = max_product

    for i in range(1, len(arr)):
        prev_max = max_product
        max_product = max(arr[i], arr[i] * max_product, arr[i] * min_product)
        min_product = min(arr[i], arr[i] * prev_max, arr[i] * min_product)

        result = max(result, max_product)

    return result

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)