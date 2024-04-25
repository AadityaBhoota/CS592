def re_arrange_array(arr, n):
    rearranged_arr = []
    
    # Step 1: Traverse the array from the beginning to n
    for i in range(n):
        # Step 2: Check for negative elements and append them to the new list
        if arr[i] < 0:
            rearranged_arr.append(arr[i])
    
    # Step 3: Traverse the array from the beginning to n again
    for i in range(n):
        # Step 4: Check for positive elements and append them to the new list
        if arr[i] >= 0:
            rearranged_arr.append(arr[i])
    
    return rearranged_arr

def check(candidate):
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

check(re_arrange_array)