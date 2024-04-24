def find_Element(arr, ranges, rotations, index):
    for r in ranges:
        start, end = r
        for _ in range(rotations % len(arr)):
            arr = arr[end+1:] + arr[:end+1]
        if index >= start and index <= end:
            return arr[index-start]

# Test cases




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)