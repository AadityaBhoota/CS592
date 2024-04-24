def max_product(arr):
    """
    Find the maximum product formed by multiplying numbers of an increasing subsequence of the given array.

    Args:
        arr (list): The input array.

    Returns:
        int: The maximum product.
    """
    n = len(arr)
    if n < 2:
        return 0

    # Sort the array in ascending order
    arr.sort()

    # Find the length of the longest increasing subsequence
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # Find the maximum product
    max_prod = 1
    for i in range(n - 1, -1, -1):
        if lis[i] == n - i:
            max_prod *= arr[i]
    return max_prod

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)