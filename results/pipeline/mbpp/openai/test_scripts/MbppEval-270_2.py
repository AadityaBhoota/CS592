def sum_even_and_even_index(arr):
    even_sum = 0
    for index, num in enumerate(arr):
        if num % 2 == 0 and index % 2 == 0:
            even_sum += num
    
    return even_sum

def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12

check(sum_even_and_even_index)