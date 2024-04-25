def max_subarray_product(arr):
    if not arr:
        return 0

    max_so_far = arr[0]
    min_so_far = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        temp = max_so_far
        max_so_far = max(max(max_so_far * arr[i], min_so_far * arr[i]), arr[i])
        min_so_far = min(min(temp * arr[i], min_so_far * arr[i]), arr[i])
        result = max(result, max_so_far)

    return result

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)