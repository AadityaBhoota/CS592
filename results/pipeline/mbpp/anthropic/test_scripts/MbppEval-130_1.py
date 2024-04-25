from collections import defaultdict

def max_occurrences(nums):
    count_dict = defaultdict(int)
    for num in nums:
        count_dict[num] += 1
    max_count = 0
    max_element = None
    for element, freq in count_dict.items():
        if freq > max_count:
            max_count = freq
            max_element = element
    return (max_element, max_count)

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)