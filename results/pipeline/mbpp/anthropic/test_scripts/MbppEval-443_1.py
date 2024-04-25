def largest_neg(list1):
    largest_negative = float('-inf')
    
    for num in list1:
        if num < 0 and num > largest_negative:
            largest_negative = num
    
    if largest_negative == float('-inf'):
        return None
    else:
        return largest_negative

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)