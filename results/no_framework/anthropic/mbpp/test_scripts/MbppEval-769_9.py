def Diff(li1, li2):
    """
    Write a python function to get the difference between two lists.

    Examples:
    (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    (Diff([1,2,3], [6,7,1])) == [2,3,6,7]
    """
    return list(set(li1) ^ set(li2))

def check(candidate):
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]

check(Diff)