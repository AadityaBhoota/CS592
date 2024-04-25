from collections import defaultdict

def max_occurrences(nums):
    occurrence_count = defaultdict(int)
    for num in nums:
        occurrence_count[num] += 1

    max_num = None
    max_count = 0

    for num, count in occurrence_count.items():
        if count > max_count:
            max_num = num
            max_count = count

    return max_num, max_count

# Test cases




def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)