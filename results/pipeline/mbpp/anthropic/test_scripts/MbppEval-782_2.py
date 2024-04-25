def odd_length_sum(arr):
    total_sum = 0
    current_sum = 0
    current_length = 0
    for num in arr:
        current_sum += num
        current_length += 1
        if current_length % 2 == 1:
            total_sum += current_sum
        else:
            current_sum = 0
    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)