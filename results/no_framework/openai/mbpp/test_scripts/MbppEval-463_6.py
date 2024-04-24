def max_subarray_product(arr):
    if not arr:
        return None

    max_ending_here = min_ending_here = result = arr[0]

    for num in arr[1:]:
        if num < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here

        max_ending_here = max(num, max_ending_here * num)
        min_ending_here = min(num, min_ending_here * num)

        result = max(result, max_ending_here)

    return result

# Test cases




def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)