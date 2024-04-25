from collections import defaultdict

def max_occurrences(nums):
    freq_map = defaultdict(int)
    
    # Count frequency of each item in the list
    for num in nums:
        freq_map[num] += 1
        
    # Find the item with maximum frequency
    max_item = None
    max_freq = 0
    for item, freq in freq_map.items():
        if freq > max_freq:
            max_item = item
            max_freq = freq
    
    return (max_item, max_freq)

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)