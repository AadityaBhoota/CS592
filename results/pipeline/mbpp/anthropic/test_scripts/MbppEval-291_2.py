def count_no_of_ways(n, k):
    if n == 1:
        return k
    
    same = k
    different = k * (k - 1)
    
    for i in range(3, n+1):
        new_same = different
        new_different = (same + different) * (k - 1)
        same = new_same
        different = new_different
    
    return same + different

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)