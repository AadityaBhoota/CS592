def odd_length_sum(arr):
    total_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if len(str(current_sum)) % 2 != 0:
            total_sum += current_sum
    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)