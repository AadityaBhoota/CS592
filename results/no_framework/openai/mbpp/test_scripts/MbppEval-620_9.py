def largest_subset(a, n):
    count = [0] * (n + 1)
    for num in a:
        count[num % n] += 1

    result = min(count[0], 1)
    for i in range(1, n//2 + 1):
        if i != n - i:
            result += max(count[i], count[n-i])
        else:
            result += min(count[i], 1)
    
    return result

# Test cases




def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)