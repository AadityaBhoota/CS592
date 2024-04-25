def count_no_of_ways(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return k
    else:
        total_ways_two_posts = k * k
        same_color, diff_color = k, k * (k - 1)

        for _ in range(2, n):
            same_color, diff_color = diff_color, (same_color + diff_color) * (k - 1)

        return same_color + diff_color

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)