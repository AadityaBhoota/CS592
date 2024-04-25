from collections import defaultdict

def max_occurrences(nums):
    """
    Write a function to find the item with maximum frequency in a given list.

    Examples:
    max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == (2, 5)
    max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18]) == (8, 2)
    max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10]) == (20, 3)
    """
    freq_dict = defaultdict(int)
    for num in nums:
        freq_dict[num] += 1

    max_freq = max(freq_dict.values())
    for num, count in freq_dict.items():
        if count == max_freq:
            return (num, count)

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)