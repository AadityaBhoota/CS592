def find_Element(arr,ranges,rotations,index) :  
    '''
    Write a python function to find element at a given index after number of rotations.

    Examples:
    find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1
    '''
def find_element(arr, ranges, rotations, index):
    
    def rotate_array(arr, rotations):
        rotations = rotations % len(arr)
        return arr[-rotations:] + arr[:-rotations]

    rotated_arr = rotate_array(arr, rotations)
    
    for start, end in ranges:
        subarray = rotated_arr[start:end+1]
        
        if index < len(subarray):
            return subarray[index]
    
    return None

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)