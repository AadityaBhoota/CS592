def count_Pairs(arr, n): 
    count = 0
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for key in freq:
        count += freq[key] * (n - freq[key])
        
    return count // 2

# Test cases




def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)