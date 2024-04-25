def odd_length_sum(arr):
    total_sum = 0
    for start in range(len(arr)):
        sum_so_far = 0
        for end in range(start, len(arr)):
            sum_so_far += arr[end]
            if (end - start + 1) % 2 == 1:
                total_sum += sum_so_far
    return total_sum

# Test cases




def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)