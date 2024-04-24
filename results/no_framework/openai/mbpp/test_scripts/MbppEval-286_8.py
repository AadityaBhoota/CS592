def max_sub_array_sum_repeated(a, n, k): 
    max_sum = float('-inf')
    
    for i in range(n):
        j = 0
        while j < n * k:
            curr_sum = 0
            for x in range(j, j + n):
                curr_sum += a[x % n]
                max_sum = max(max_sum, curr_sum)
            j += n
            
    return max_sum

# Test the function with the provided examples




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)