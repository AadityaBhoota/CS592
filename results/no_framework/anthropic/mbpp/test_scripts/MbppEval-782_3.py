def odd_length_sum(arr):
    """
    Write a python function to find the sum of all odd length subarrays.
    Examples:
    Odd_Length_Sum([1,2,4]) == 14
    Odd_Length_Sum([1,2,1,2]) == 15
    Odd_Length_Sum([1,7]) == 8
    """
    total_sum = 0
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j+1]
            if len(subarray) % 2 != 0:
                total_sum += sum(subarray)
    
    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)