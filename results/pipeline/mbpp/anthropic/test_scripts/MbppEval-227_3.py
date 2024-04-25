def min_of_three(a, b, c):
    minimum = a
    
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    
    return minimum

def check(candidate):
    assert min_of_three(10,20,0)==0
    assert min_of_three(19,15,18)==15
    assert min_of_three(-10,-20,-30)==-30

check(min_of_three)