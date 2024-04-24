def max_subarray_product(arr):
    # Initialize variables to keep track of the maximum and minimum product ending at the current index
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            # Swap max_prod and min_prod as multiplying by a negative number can change the sign
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(arr[i], max_prod * arr[i])
        min_prod = min(arr[i], min_prod * arr[i])

        result = max(result, max_prod)

    return result

# Test cases




def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)