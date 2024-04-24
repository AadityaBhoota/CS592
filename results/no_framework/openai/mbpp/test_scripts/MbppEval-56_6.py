def check(num):
    reverse_num = int(str(num)[::-1])
    return num == 2*reverse_num + 1

# Test examples




def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)