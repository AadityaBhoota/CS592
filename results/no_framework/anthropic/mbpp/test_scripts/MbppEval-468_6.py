def max_product(arr):
    """
    Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
    """
    n = len(arr)
    if n < 2:
        return 0

    # Sort the array in ascending order
    arr.sort()

    # Initialize the maximum product
    max_prod = 0

    # Iterate through the array and find the maximum product
    for i in range(n - 1):
        prod = 1
        for j in range(i, n):
            prod *= arr[j]
            max_prod = max(max_prod, prod)

    return max_prod

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)