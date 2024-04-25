def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]
    count = 0

    a_mod_3 = [x for x in a if x % 3 == 0]
    count += len(a_mod_3)

    for x in a_mod_3:
        count += a.count(3 * (x // 3) - x)

    return count

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)