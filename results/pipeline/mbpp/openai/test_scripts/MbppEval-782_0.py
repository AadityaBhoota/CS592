def odd_length_sum(arr):
    def generate_subarrays(arr, length):
        subarrays = []
        for i in range(len(arr) - length + 1):
            subarrays.append(arr[i:i+length])
        return subarrays
    
    total_sum = 0
    for length in range(1, len(arr)+1, 2):
        subarrays = generate_subarrays(arr, length)
        for subarray in subarrays:
            total_sum += sum(subarray)
    
    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)