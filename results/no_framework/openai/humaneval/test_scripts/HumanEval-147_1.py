def get_max_triples(n):
    count = 0

    for i in range(1, n+1):
        a = i * i - i + 1
        for j in range(i+1, n+1):
            b = j * j - j + 1
            for k in range(j+1, n+1):
                c = k * k - k + 1
                if (a + b + c) % 3 == 0:
                    count += 1

    return count

# Test the function with the example provided
n = 5


def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)