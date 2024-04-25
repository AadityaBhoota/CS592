def count_no_of_ways(n, k):
    if n == 1:
        return k
    
    same = k
    diff = k * (k-1)
    
    for i in range(3, n+1):
        same, diff = diff, (same + diff) * (k-1)
    
    return same + diff

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)