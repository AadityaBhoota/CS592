def count_Pairs(arr, n):
    unique_elements = set(arr)
    return n * (n - 1) // 2 - len(unique_elements)

def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)