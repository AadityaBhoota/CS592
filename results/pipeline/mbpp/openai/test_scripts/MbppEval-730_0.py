from itertools import groupby

def consecutive_duplicates(nums):
    result = []
    
    for index, num in enumerate(nums):        
        if index == 0 or num != nums[index - 1]:
            result.append(num)
    
    return result

def check(candidate):
    assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    assert consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[10, 15, 19, 18, 17, 26, 17, 18, 10]
    assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==['a', 'b', 'c', 'd']
    assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd', 'a', 'a'])==['a', 'b', 'c', 'd', 'a']

check(consecutive_duplicates)