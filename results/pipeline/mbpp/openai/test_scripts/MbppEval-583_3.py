def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def catalan_number(num):
    result = 1
    for i in range(1, num+1):
        result = result * (2 * (2 * i - 1)) // (i + 1)
    
    return result

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)