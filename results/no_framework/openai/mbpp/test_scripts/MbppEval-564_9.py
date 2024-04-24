def count_Pairs(arr, n):
    unique_values = set(arr)
    count = 0
    for val in unique_values:
        count += arr.count(val) * (n - arr.count(val))
    return count // 2

# Test cases




def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)