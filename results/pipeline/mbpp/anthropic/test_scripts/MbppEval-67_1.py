from math import comb

def bell_number(n):
    bell_list = [0] * (n + 1)
    bell_list[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            bell_list[i] += bell_list[j] * comb(i - 1, j)

    return bell_list[n]

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)