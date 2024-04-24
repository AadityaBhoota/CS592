def sum_in_range(l, r):
    total = 0
    for num in range(l, r+1):
        if num % 2 != 0:  # Check if the number is odd
            total += num
    return total

# Test the function




def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)