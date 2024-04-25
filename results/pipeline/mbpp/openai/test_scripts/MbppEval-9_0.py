def find_Rotations(input_str): 
    if len(input_str) <= 1:
        return 0
        
    rotation = 0
    
    for i in range(1, len(input_str)//2 + 1):
        rotated_str = input_str[i:] + input_str[:i]
        
        if rotated_str == input_str:
            rotation = i
            break
    
    return rotation

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)