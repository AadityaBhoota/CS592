def largest_neg(list1):
    if not list1:
        return None
    
    largest_neg = None
    
    for num in list1:
        if num < 0:
            if largest_neg is None or num > largest_neg:
                largest_neg = num
    
    return largest_neg

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)