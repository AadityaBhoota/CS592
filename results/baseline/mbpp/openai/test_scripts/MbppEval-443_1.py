def largest_neg(list1):
    neg_numbers = [num for num in list1 if num < 0]
    if neg_numbers:
        return max(neg_numbers)
    else:
        return None

# Test cases




def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)