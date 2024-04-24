def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            result.append(sum(range(1, i+1)))
    return result

# Test the function


def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

check(f)