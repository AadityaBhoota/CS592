def max_sum(arr):
    # Step 0: Finding the longest increasing subsequence array
    def longest_increasing_subsequence(arr):
        lis = [arr[i] for i in range(len(arr))]
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] > arr[j] and lis[i] < lis[j] + arr[i]:
                    lis[i] = lis[j] + arr[i]
        return lis

    # Step 1: Finding the longest increasing subsequence array
    lis = longest_increasing_subsequence(arr)

    # Step 2: Finding the longest decreasing subsequence array from the right side
    def longest_decreasing_subsequence(arr):
        lds = [arr[i] for i in range(len(arr))]
        for i in range(len(arr) - 2, -1, -1):
            for j in range(len(arr) - 1, i, -1):
                if arr[i] > arr[j] and lds[i] < lds[j] + arr[i]:
                    lds[i] = lds[j] + arr[i]
        return lds

    # Step 3: Finding the maximum sum of a bitonic subsequence
    lds = longest_decreasing_subsequence(arr)
    max_sum = 0
    for i in range(len(arr)):
        bitonic_sum = lis[i] + lds[i] - arr[i]
        if bitonic_sum > max_sum:
            max_sum = bitonic_sum

    return max_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)