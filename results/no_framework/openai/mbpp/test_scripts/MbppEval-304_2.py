def find_Element(arr, ranges, rotations, index):
    for i in range(rotations):
        a, b = ranges[i % len(ranges)]
        arr = arr[a:b+1] + arr[:a] + arr[b+1:]
    
    return arr[index]

# Examples




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)