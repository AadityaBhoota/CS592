def find_Rotations(str): 
    count = 1
    if len(str) == 1:
        return count
    
    rotated = str
    while rotated != str:
        count += 1
        rotated = rotated[-1] + rotated[:-1]
    
    return count

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)