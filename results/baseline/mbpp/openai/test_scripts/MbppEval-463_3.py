def max_subarray_product(arr):
    if not arr:
        return 0

    current_max = current_min = max_product = arr[0]

    for num in arr[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        max_product = max(max_product, current_max)

    return max_product

# Test cases




def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)