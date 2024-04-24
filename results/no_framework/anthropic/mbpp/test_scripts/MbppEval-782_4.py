def odd_length_sum(arr):
    """
    Find the sum of all odd length subarrays in the given array.
    
    Args:
        arr (list): The input array.
    
    Returns:
        int: The sum of all odd length subarrays.
    """
    total_sum = 0
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j+1]
            if len(subarray) % 2 == 1:
                total_sum += sum(subarray)
    
    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)