def max_product(arr):
    if len(arr) == 0:
        return 0

    max_pos = [1] + [0] * (len(arr) - 1)
    min_neg = [1] + [0] * (len(arr) - 1)

    for i in range(1, len(arr)):
        if arr[i] > 0:
            max_pos[i] = max(arr[i], max_pos[i - 1] * arr[i])
            min_neg[i] = min(arr[i], min_neg[i - 1] * arr[i])
        elif arr[i] < 0:
            max_pos[i] = max(arr[i], min_neg[i - 1] * arr[i])
            min_neg[i] = min(arr[i], max_pos[i - 1] * arr[i])
        else:
            max_pos[i] = min_neg[i] = 0

    return max(max_pos)

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)