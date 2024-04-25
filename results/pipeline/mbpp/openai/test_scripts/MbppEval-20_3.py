def is_woodall(x): 
    if x <= 1:
        return False
    
    n = 1
    while n * (2 ** n - 1) < x:
        n += 1
    
    if x == n * (2 ** n - 1):
        return True
    else:
        return False

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)