from collections import defaultdict

def max_occurrences(nums):
    # Count the frequency of each number in the list
    freq_dict = defaultdict(int)
    for num in nums:
        freq_dict[num] += 1
    
    # Find the number with maximum frequency
    max_freq = 0
    max_num = None
    for num, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_num = num
    
    return (max_num, max_freq)

# Test the function with the provided examples




def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)