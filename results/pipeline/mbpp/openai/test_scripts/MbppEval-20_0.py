def is_woodall(x):
    n = 1
    while n * (2**n - 1) < x:
        n += 1
    woodall_num = n * (2**n - 1)
    
    return woodall_num == x

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)