def get_pairs_count(arr, target_sum):
    """
    Counts the number of pairs in the given array whose sum is equal to the target sum.
    
    Args:
        arr (list): The list of numbers.
        target_sum (int): The target sum.
        
    Returns:
        int: The count of pairs whose sum is equal to the target sum.
    """
    count = 0
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += 1
        seen.add(num)
    
    return count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)