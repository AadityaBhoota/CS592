def min_of_three(a, b, c):
    if a < b:
        min_value = a
    else:
        min_value = b
        
    if c < min_value:
        min_value = c

    return min_value

def check(candidate):
    assert min_of_three(10,20,0)==0
    assert min_of_three(19,15,18)==15
    assert min_of_three(-10,-20,-30)==-30

check(min_of_three)