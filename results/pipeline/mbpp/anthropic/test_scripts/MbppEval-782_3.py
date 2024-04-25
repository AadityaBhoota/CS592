def odd_length_sum(arr):
    total_sum = sum(arr)
    odd_sum = sum(arr[i] ** 2 for i in range(len(arr)) if i % 2 != 0)
    return total_sum + odd_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)