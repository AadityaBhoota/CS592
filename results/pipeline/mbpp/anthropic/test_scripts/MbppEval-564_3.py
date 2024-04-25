def count_Pairs(arr, n):
    element_counts = {}
    for num in arr:
        if num in element_counts:
            element_counts[num] += 1
        else:
            element_counts[num] = 1
    
    total_pairs = 0
    for count in element_counts.values():
        total_pairs += count * (n - count)
    
    return total_pairs // 2

def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)