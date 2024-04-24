def count_no_of_ways(n, k):
    if n == 0:
        return 0

    same_color_count = [0] * n
    diff_color_count = [0] * n

    # Base cases
    same_color_count[0] = k
    diff_color_count[0] = k

    for i in range(1, n):
        # For same color at i-th post, previous post should have different color, so there are k-1 choices
        same_color_count[i] = diff_color_count[i-1]

        # For different color at i-th post, we can either paint it with one of the k-1 colors different from previous post
        # Or paint it with the same color as previous post, which happens only if the previous post was a different color as the post before that
        diff_color_count[i] = (k-1) * (same_color_count[i-1] + diff_color_count[i-1])

    return same_color_count[-1] + diff_color_count[-1]

# Test cases




def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)