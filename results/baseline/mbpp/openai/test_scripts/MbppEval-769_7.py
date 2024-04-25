def Diff(li1, li2):
    result = [item for item in li1 if item not in li2]
    result.extend([item for item in li2 if item not in li1])
    return result

# Test cases




def check(candidate):
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]

check(Diff)