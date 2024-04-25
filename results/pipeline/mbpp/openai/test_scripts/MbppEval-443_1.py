def largest_neg(list1): 
    largest_neg_num = None
    
    for num in list1:
        if num < 0:
            if largest_neg_num is None or num > largest_neg_num:
                largest_neg_num = num
    
    return largest_neg_num

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)