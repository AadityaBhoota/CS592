# Step 1: Define the function large_product
def large_product(nums1, nums2, N):
    # Step 2: Multiply each element in nums1 with each element in nums2 to generate a list of products
    products = [x * y for x in nums1 for y in nums2]
    
    # Step 3: Sort the list of products in descending order
    products.sort(reverse=True)
    
    # Step 4: Return the first N elements of the sorted list
    return products[:N]

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)