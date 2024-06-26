def monotonic(l: list):
    increasing = True
    decreasing = True
    
    for i in range(1, len(l)):
        if l[i] <= l[i-1]:
            increasing = False
        if l[i] >= l[i-1]:
            decreasing = False
    
    return increasing or decreasing



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True


check(monotonic)