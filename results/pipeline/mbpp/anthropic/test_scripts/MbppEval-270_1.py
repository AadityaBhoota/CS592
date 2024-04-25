def sum_even_and_even_index(arr):
    sum = 0
    for i, num in enumerate(arr):
        if num % 2 == 0 and i % 2 == 0:
            sum += num
    return sum

def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12

check(sum_even_and_even_index)