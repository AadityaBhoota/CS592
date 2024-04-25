def rotate(arr, times):
    n = len(arr)
    times = times % n
    
    return arr[-times:] + arr[:-times]

def find_Element(arr, ranges, rotations, index):
    for r in ranges:
        arr = rotate(arr, r[1] - r[0])
    
    rotated_arr = rotate(arr, rotations)
    
    return rotated_arr[index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)