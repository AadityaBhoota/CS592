import math

def eulerian_num(n, m): 
    '''
    Write a function to find the Eulerian number a(n, m).

    Examples:
    eulerian_num(3, 1) == 4
    eulerian_num(4, 1) == 11
    eulerian_num(5, 3) == 26
    '''
    def binomial_coefficient(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    
    def eulerian_number(n, m):
        result = 0
        for k in range(m + 1):
            result += ((-1) ** k) * binomial_coefficient(n + 1, k) * ((m + 1 - k) ** n)
        return result
    
    return eulerian_number(n, m)

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)