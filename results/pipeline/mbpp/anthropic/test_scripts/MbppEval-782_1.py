def odd_length_sum(arr):
    total_sum = 0
    prefix_sum = [0] * (len(arr) + 1)
    
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
    
    for i in range(1, len(arr) + 1):
        odd_length_subarrays = (i + 1) // 2
        total_sum += odd_length_subarrays * arr[i-1]
    
    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)