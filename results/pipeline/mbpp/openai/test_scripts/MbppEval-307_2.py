from copy import deepcopy
def colon_tuplex(tuplex,m,n):
    '''
    Write a function to get a colon of a tuple.

    Examples:
    colon_tuplex(("HELLO", 5, [], True) ,2,50) == ("HELLO", 5, [50], True)
    colon_tuplex(("HELLO", 5, [], True) ,2,100) == (("HELLO", 5, [100],True))
    colon_tuplex(("HELLO", 5, [], True) ,2,500) == ("HELLO", 5, [500], True)
    '''

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)