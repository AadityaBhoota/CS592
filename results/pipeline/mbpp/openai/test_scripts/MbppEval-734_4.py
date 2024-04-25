def sum_Of_Subarray_Prod(arr):
    products = []
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            sublist_product = 1
            
            for num in arr[i:j]:
                sublist_product *= num
            
            products.append(sublist_product)
    
    return sum(products)

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)