def max_product(arr, n):   
    max_ending_here = min_ending_here = max_so_far = arr[0]
    for i in range(1, n):
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here
        max_ending_here = max(arr[i], max_ending_here * arr[i])
        min_ending_here = min(arr[i], min_ending_here * arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)