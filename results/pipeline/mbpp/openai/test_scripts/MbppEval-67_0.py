import math

def bell_number(n):   
    if n < 0:
        return 0
    
    bell = [0] * (n + 1)
    bell[0] = 1
    
    for j in range(1, n + 1):
        for i in range(1, j + 1):
            bell[j] += bell[j - i] * math.factorial(j - 1) // (math.factorial(i) * math.factorial(j - i))
    
    return bell[n]

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)