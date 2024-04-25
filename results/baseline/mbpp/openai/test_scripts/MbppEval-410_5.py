def min_val(listval):
    # Filter out non-numeric elements and convert numeric elements to integers
    nums = [int(val) for val in listval if isinstance(val, (int, float))]
    
    # Find the minimum value in the list of numbers
    min_num = min(nums)
    
    return min_num

# Test cases




def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)