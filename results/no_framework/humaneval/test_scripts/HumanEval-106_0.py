def f(n):
    def factorial(num):
        if num == 0:
            return 1
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))

    return result

# Test the function with the example given in the problem description


def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

check(f)