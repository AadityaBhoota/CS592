def max_subarray_product(arr):
    if not arr:
        return 0

    max_so_far = arr[0]
    min_so_far = arr[0]
    result = max_so_far

    for i in range(1, len(arr)):
        curr = arr[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max

        result = max(max_so_far, result)

    return result

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)