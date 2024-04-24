def find_kth(arr1, arr2, m, n, k):
    if m > n:
        return find_kth(arr2, arr1, n, m, k)
    if m == 0:
        return arr2[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(m, k // 2)
    j = min(n, k // 2)

    if arr1[i - 1] > arr2[j - 1]:
        return find_kth(arr1, arr2[j:], m, n - j, k - j)
    else:
        return find_kth(arr1[i:], arr2, m - i, n, k - i)

# Test the function with the given examples




def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)