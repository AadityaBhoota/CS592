def max_subarray_product(arr):
    if not arr:
        return 0

    max_ending_here = min_ending_here = max_product = arr[0]

    for num in arr[1:]:
        temp_max = max_ending_here
        max_ending_here = max(num, num * max_ending_here, num * min_ending_here)
        min_ending_here = min(num, num * temp_max, num * min_ending_here)
        max_product = max(max_product, max_ending_here)

    return max_product

# Test cases




def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)