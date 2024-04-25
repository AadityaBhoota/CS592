def odd_length_sum(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i, len(arr), 2):
            total += sum(arr[i:j+1])
    return total

# Test cases




def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)