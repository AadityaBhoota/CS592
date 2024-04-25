from collections import defaultdict

def max_occurrences(nums):
    counts = defaultdict(int)
    
    for num in nums:
        counts[num] += 1

    max_num = max(counts, key=counts.get)
    
    return (max_num, counts[max_num])

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)