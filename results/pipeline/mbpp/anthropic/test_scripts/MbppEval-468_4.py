def max_product(arr):
    """
    Find the maximum product formed by multiplying numbers of an increasing subsequence of the given array.
    """
    n = len(arr)
    max_prod = arr[0]
    prev_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], prev_max * arr[i])
        max_prod = max(max_prod, curr_max)
        prev_max = curr_max

    return max_prod

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)