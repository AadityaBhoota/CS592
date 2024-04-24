from collections import Counter

def get_pairs_count(arr, n, target):
    count = 0
    freq = Counter(arr)
    
    for num in arr:
        diff = target - num
        if diff in freq:
            count += freq[diff]
        
        if diff == num:
            count -= 1
    
    return count // 2

# Examples




def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)