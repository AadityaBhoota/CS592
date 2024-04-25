def min_of_three(a, b, c):
    min_num = a if a < b else b
    min_num = c if c < min_num else min_num
    return min_num

def check(candidate):
    assert min_of_three(10,20,0)==0
    assert min_of_three(19,15,18)==15
    assert min_of_three(-10,-20,-30)==-30

check(min_of_three)