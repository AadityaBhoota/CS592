def largest_neg(list1): 
    neg_nums = [num for num in list1 if num < 0]
    if neg_nums:
        return max(neg_nums)
    else:
        return None

# Test cases




def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)