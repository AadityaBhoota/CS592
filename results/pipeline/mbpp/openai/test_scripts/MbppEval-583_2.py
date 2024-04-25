import math

def catalan_number(num):
    return math.factorial(2*num) // (math.factorial(num + 1) * math.factorial(num))

n = 10
catalan_10 = catalan_number(n)


def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)