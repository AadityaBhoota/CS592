def bell_number(n):
    bell = [[0 for _ in range(n)] for _ in range(n)]
    bell[0][0] = 1
    
    return bell

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)