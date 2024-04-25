def f(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(factorial(i+1))
        else:
            result.append(sum(range(1, i+2)))
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

check(f)