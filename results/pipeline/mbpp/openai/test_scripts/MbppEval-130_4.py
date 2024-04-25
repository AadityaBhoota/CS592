from collections import defaultdict

def max_occurrences(nums):
    freq_dict = defaultdict(int)
    
    # Count the frequency of each item in the list
    for item in nums:
        freq_dict[item] += 1
        
    # Find the item with the maximum frequency
    max_item = max(freq_dict, key=freq_dict.get)
    
    return max_item, freq_dict[max_item]

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)