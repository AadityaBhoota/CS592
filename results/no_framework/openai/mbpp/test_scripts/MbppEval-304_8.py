def find_Element(arr, ranges, rotations, index):
    n = len(arr)
    
    for rotation in range(rotations):
        a, b = ranges[rotation % len(ranges)]
        arr = arr[a:b+1][::-1] + arr[b+1:] + arr[:a]
    
    return arr[index]

# Test cases




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)