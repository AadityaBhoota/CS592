def largest_subset(a, n):
    count = [0] * n
    result = 0
    for num in a:
        count[num % n] += 1
    half = n // 2
    if count[0] > 0:
        result += 1
    for i in range(1, half + 1):
        result += max(count[i], count[n - i])
    if n % 2 == 0 and count[half] > 0:
        result += 1
    return result

# Examples




def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)