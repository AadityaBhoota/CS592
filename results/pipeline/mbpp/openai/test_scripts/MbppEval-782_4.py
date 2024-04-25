def odd_length_sum(arr):
    result = 0
    n = len(arr)
    for start in range(n):
        for end in range(start, n):
            sub_arr = arr[start:end+1]
            if len(sub_arr) % 2 == 1:
                sub_arr_sum = sum(sub_arr)
                result += sub_arr_sum
    return result

def check(candidate):
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,1,2]) == 15
    assert odd_length_sum([1,7]) == 8

check(odd_length_sum)