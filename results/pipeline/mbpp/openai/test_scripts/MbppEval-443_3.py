def largest_neg(list1): 
    negative_numbers = [num for num in list1 if num < 0]
    
    if not negative_numbers:
        return None
    
    largest_neg_num = max(negative_numbers)
    return largest_neg_num

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)