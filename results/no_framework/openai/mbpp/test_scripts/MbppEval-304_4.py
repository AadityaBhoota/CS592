def find_Element(arr, ranges, rotations, index):
    for r in ranges:
        left, right = r
        for _ in range(rotations):
            arr[left], arr[right] = arr[right], arr[left]
    return arr[index]

# Test cases




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)