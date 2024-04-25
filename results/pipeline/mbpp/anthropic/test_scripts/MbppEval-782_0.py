def odd_length_sum(arr):
    total_sum = 0
    left = 0
    right = 0

    while right < len(arr):
        if (right - left + 1) % 2 != 0:
            total_sum += sum(arr[left:right+1])
        right += 1

        if (right - left + 1) % 2 == 0:
            left += 1

    return total_sum

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)