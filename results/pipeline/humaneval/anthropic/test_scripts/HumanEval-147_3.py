def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]
    count_0 = count_1 = count_2 = 0
    for x in a:
        remainder = x % 3
        if remainder == 0:
            count_0 += 1
        elif remainder == 1:
            count_1 += 1
        else:
            count_2 += 1
    return count_0 * count_1 * count_2

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)