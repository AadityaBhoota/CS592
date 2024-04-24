def check(num):    
    return num == 2 * int(str(num)[::-1]) - 1

# Test cases




def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)