def max_sub_array_sum_repeated(a, n, k): 
    def kadane(arr):
        max_sum = float('-inf')
        curr_sum = 0
        
        for num in arr:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
    combined_array = a * k
    return kadane(combined_array)

# Test cases




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)