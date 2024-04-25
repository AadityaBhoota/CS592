def count_Pairs(arr, n):
    count = 0
    freq_map = {}
    
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    for key in freq_map:
        count += (freq_map[key] * (freq_map[key] - 1)) // 2
    
    return count

# Test cases




def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)