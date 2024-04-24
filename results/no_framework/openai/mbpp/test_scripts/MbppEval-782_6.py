def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    
    for start in range(n):
        for length in range(1, n - start + 1, 2):
            subarray = arr[start:start+length]
            total_sum += sum(subarray)
    
    return total_sum

# Test cases




def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)