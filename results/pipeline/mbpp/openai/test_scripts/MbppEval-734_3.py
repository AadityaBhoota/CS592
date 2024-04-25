def sum_Of_Subarray_Prod(arr):
    def subarray_product(arr):
        product = 1
        for num in arr:
            product *= num
        return product

    result = 0
    n = len(arr)
    
    for length in range(1, n+1):
        for i in range(n-length+1):
            sublist = arr[i:i+length]
            product = subarray_product(sublist)
            result += product

    return result

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)