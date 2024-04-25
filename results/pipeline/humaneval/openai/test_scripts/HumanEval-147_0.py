def get_max_triples(n):
    result = []
    count = 0

    for i in range(1, n + 1):
        a_i = i * i - i + 1
        result.append(a_i)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (result[i] + result[j] + result[k]) % 3 == 0:
                    count += 1

    return count

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)