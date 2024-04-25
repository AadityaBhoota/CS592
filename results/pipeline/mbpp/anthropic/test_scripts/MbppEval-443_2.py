def largest_neg(list1):
    largest_neg = float('-inf')
    for num in list1:
        if num < 0 and num > largest_neg:
            largest_neg = num
    return largest_neg

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)