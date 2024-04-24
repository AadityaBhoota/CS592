def find_Element(arr, ranges, rotations, index):
    n = len(arr)
    
    # Function to rotate array elements by 'r' positions
    def rotate(arr, r):
        return arr[r:] + arr[:r]
    
    for l, r in ranges:
        # Get the range of elements to rotate
        subarr = arr[l:r+1]
        subarr_rotated = rotate(subarr, rotations % len(subarr))
        arr[l:r+1] = subarr_rotated
    
    return arr[index]

# Examples




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)