def largest_subset(a, n):
    count = {}
    for num in a:
        count[num] = 1

    max_length = 0

    for num in a:
        length = count[num]
        for multiple in range(2*num, n+1, num):
            if multiple in count:
                count[multiple] = max(count[multiple], length + 1)
        max_length = max(max_length, length)

    return max_length

# Test cases




def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)