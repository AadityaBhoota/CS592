def find_kth(arr1, arr2, k):
    m, n = len(arr1), len(arr2)

    def binary_search(start1, end1, start2, end2):
        if start1 > end1:
            return arr2[start2 + k - 1]
        if start2 > end2:
            return arr1[start1 + k - 1]
        if k == 1:
            return min(arr1[start1], arr2[start2])

        mid1 = (start1 + end1) // 2
        mid2 = (start2 + end2) // 2
        if arr1[mid1] < arr2[mid2]:
            return binary_search(mid1 + 1, end1, start2, end2)
        else:
            return binary_search(start1, end1, mid2 + 1, end2)

    return binary_search(0, m - 1, 0, n - 1)

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)