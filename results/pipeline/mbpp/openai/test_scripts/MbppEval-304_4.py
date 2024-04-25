def find_Element(arr, ranges, rotations, index):
    cur_index = index
    
    for rotation in rotations:
        actual_rotation = rotation % len(arr)
        cur_index = (cur_index + actual_rotation) % len(arr)
    
    return arr[cur_index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)