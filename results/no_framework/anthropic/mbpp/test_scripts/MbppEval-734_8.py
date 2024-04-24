def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total_sum = 0

    for i in range(1, n + 1):
        for j in range(n - i + 1):
            subarray = arr[j:j + i]
            product = 1
            for num in subarray:
                product *= num
            total_sum += product

    return total_sum

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)