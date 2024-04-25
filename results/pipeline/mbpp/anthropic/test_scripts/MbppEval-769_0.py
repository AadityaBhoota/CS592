def Diff(li1, li2):
    output = []
    for item in li1:
        if item not in li2:
            output.append(item)
    for item in li2:
        if item not in li1:
            output.append(item)
    return output

def check(candidate):
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]

check(Diff)