def odd_length_sum(arr):
    total_sum = 0
    
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            subarray_length = end - start + 1
            
            if subarray_length % 2 != 0:
                total_sum += sum(arr[start:end+1])
    
    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)