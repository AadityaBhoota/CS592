def rev(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    
    return num == 2 * rev_num - 1

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)