def sum_Of_Subarray_Prod(arr):
    '''
    Write a python function to find sum of products of all possible sublists of a given list. 
    Examples:
    sum_Of_Subarray_Prod([1,2,3],3) == 20
    sum_Of_Subarray_Prod([1,2],2) == 5
    sum_Of_Subarray_Prod([1,2,3,4],4) == 84
    '''
    def generate_subarrays(arr):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                subarrays.append(arr[i:j])
        return subarrays

    subarrays = generate_subarrays(arr)
    products = [1]  # Initialize with 1 to avoid multiplying by 0
    for subarray in subarrays:
        product = 1
        for num in subarray:
            product *= num
        products.append(product)

    return sum(products)

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)