import math

def catalan_number(n):
    if n == 0:
        return 1
    catalan = math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    return catalan

# Testing the function with the examples given




def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)