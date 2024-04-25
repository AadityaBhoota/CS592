def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n, 2):
            total_sum += sum(arr[i:j+1])
    return total_sum

# Test cases




def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)