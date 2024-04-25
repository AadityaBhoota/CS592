def sum_odd(l, r): 
    if l % 2 == 0:  # If l is even, make it odd by adding 1
        l += 1
    odd_sum = sum(range(l, r+1, 2))  # Sum of all odd numbers within the range
    return odd_sum

# Test cases




def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)