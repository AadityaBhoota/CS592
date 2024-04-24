def re_arrange_array(arr, n):
    # Initialize two pointers, one for negative elements and one for positive elements
    neg_ptr = 0
    pos_ptr = 0

    # Iterate through the array
    for i in range(n):
        # If the current element is negative, swap it with the element at the negative pointer
        if arr[i] < 0:
            arr[i], arr[neg_ptr] = arr[neg_ptr], arr[i]
            neg_ptr += 1
        # If the current element is positive, move the positive pointer forward
        else:
            pos_ptr += 1

    return arr

def check(candidate):
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

check(re_arrange_array)