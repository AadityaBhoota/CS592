def largest_neg(list1): 
    largest_negative = None
    
    for num in list1:
        if num < 0:
            if largest_negative is None or num < largest_negative:
                largest_negative = num

    return largest_negative

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)