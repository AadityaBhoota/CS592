def count_Pairs(arr, n):
    if n < 2:
        return 0
    return n * (n-1) // 2

def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)