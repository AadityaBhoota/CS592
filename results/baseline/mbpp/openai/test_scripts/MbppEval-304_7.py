def find_Element(arr, ranges, rotations, index):
    for r in ranges:
        for i in range(rotations):
            arr[r[0]:r[1]+1] = arr[r[0]+1:r[1]+1] + [arr[r[0]]]

    return arr[index]

# Test cases




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)