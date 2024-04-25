def rev(num):
    num_str = str(num)
    reversed_num_str = num_str[::-1].lstrip('0')
    return int(reversed_num_str)

def check(num):
    doubled_num = num * 2
    reversed_doubled_num = rev(doubled_num)
    return num - 1 == reversed_doubled_num

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)