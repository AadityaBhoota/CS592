def max_subarray_product(arr):
    if not arr:
        return 0

    max_prod = arr[0]
    min_prod = arr[0]
    max_so_far = arr[0]

    for num in arr[1:]:
        max_prod, min_prod = max(num, num * max_prod, num * min_prod), min(num, num * max_prod, num * min_prod)

        max_so_far = max(max_so_far, max_prod)

    return max_so_far

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)