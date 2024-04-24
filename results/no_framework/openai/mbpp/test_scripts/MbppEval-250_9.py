def count_X(tup, x):
    count = 0
    for elem in tup:
        if elem == x:
            count += 1
    return count

# Test cases




def check(candidate):
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4

check(count_X)