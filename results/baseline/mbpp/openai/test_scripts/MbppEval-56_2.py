def rev(num):    
    num_str = str(num)
    reversed_num = int(num_str[::-1])
    
    if num == 2*reversed_num - 1:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)