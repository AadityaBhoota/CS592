def odd_length_sum(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr), 2):
            result += sum(arr[i:j+1])
    return result

# Test cases




def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)