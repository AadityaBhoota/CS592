def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    
    for i in range(n):
        total_sum += arr[i] * ((i + 1) * (n - i) + 1) // 2  # calculating the contribution of each element
        
    return total_sum

# Test cases




def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)