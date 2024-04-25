def max_sub_array_sum_repeated(a, n, k):
    modified_list = a * k
    max_sum_found = float('-inf')

    for i in range(len(modified_list) - n + 1):
        subarray = modified_list[i:i+n]
        subarray_sum = sum(subarray)
        max_sum_found = max(max_sum_found, subarray_sum)

    return max_sum_found

# Test the function with the examples provided




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)