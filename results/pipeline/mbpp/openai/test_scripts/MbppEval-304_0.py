def find_Element(arr, ranges, rotations, index):
    current_index = index
    
    for i in range(rotations):
        for r in ranges:
            start, end = r
            if current_index >= start and current_index <= end:
                current_index = end - (current_index - start)
    
    return arr[current_index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)