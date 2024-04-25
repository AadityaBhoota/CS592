from collections import defaultdict

def max_occurrences(nums):
    freq_dict = defaultdict(int)
    
    for num in nums:
        freq_dict[num] += 1
    
    max_value = max(freq_dict.values())
    max_key = max(freq_dict, key=freq_dict.get)
    
    return max_key, max_value

# Test the function with examples from the docstring




def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)