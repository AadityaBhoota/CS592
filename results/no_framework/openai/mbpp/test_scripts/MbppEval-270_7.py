def sum_even_and_even_index(arr, n):
    total_sum = 0
    for i in range(n):
        if i % 2 == 0 and arr[i] % 2 == 0:
            total_sum += arr[i]
    return total_sum

def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12

check(sum_even_and_even_index)