def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def catalan_number(n):
    return factorial(2*n) // (factorial(n) * factorial(n+1))

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)