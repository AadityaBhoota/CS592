def find_min_diff(arr, n):
    arr.sort()  # Step 1: Sort the array in ascending order
    min_diff = float('inf')  # Step 2: Initialize a variable min_diff to store the minimum difference
    
    for i in range(1, n):  # Step 3: Iterate through the array from the second element to the last element
        diff = arr[i] - arr[i-1]  # Step 4: Calculate the difference between the current element and the previous element
        if diff < min_diff:  # Step 5: If the difference is less than the current minimum difference, update the minimum difference
            min_diff = diff
    
    return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)