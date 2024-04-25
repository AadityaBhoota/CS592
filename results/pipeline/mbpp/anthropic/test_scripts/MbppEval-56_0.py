def rev(num):
    reversed_num = int(str(num)[::-1])
    return num == 2 * reversed_num - 1

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)