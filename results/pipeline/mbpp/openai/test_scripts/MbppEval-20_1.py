def is_woodall(x):
    if x <= 1:
        return False
    
    woodall_number = 1
    
    while woodall_number <= x:
        woodall_value = woodall_number * (2 ** woodall_number - 1)
        
        if woodall_value == x:
            return True
        
        woodall_number += 1
    
    return False

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)