def get_max_triples(n):
    a = []
    for i in range(1, n+1):
        a.append(i * i - i + 1)

    divisible_by_3 = [x for x in a if x % 3 == 0]
    count = 0

    for i in range(len(divisible_by_3)):
        for j in range(i+1, len(divisible_by_3)):
            k = 3 - (divisible_by_3[i] + divisible_by_3[j]) % 3
            if k in a:
                count += 1

    return count

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)